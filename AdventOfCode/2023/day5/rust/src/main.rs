use std::cmp::min;
use std::fmt::Formatter;
use std::fs;
use std::str::FromStr;
use std::fmt;
use std::vec;


#[derive(Debug)]
struct MapEntry {
    src_start: i64,
    dst_start: i64,
    len: i64,
}

#[derive(Debug)]
struct Range  {
    start: i64,
    end: i64
}

impl fmt::Display for Range {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "[{} {}]", self.start, self.end)
    }
}

impl Clone for Range {
    fn clone(&self) -> Self {
        Range { start: self.start, end: self.end }
    }
}

impl Range {
    fn split(&self, r: Range) -> (Vec<Range>, Vec<Range>) {
        let mut inside: Vec<Range> = vec![];
        let mut outside: Vec<Range> = vec![];
        
        if self.end < r.start || r.end < self.start {
            outside.push(self.clone());
        } else {

            if self.start < r.start && r.end < self.end {
                // [()]
                inside.push(r.clone());
                outside.append(&mut vec![
                    Range { start: self.start, end: r.start - 1 },
                    Range { start: r.end + 1, end: self.end }
                ])
            } else if r.start < self.start && self.end < r.end { 
                // ([])
                inside.push(self.clone());
            } else if r.start < self.start && self.start < r.end && r.end < self.end {
                // ([)]
                inside.push(Range { start: self.start, end: r.end });
                outside.push(Range { start: r.end + 1, end: self.end });
            } else if self.start < r.start && r.start < self.end && self.end < r.end {
                // [(])
                inside.push(Range { start: r.start, end: self.end });
                outside.push(Range { start: self.start, end: r.start - 1 });
            } else if r.end == self.start {
                // ()
                //  []
                inside.push(Range { start: r.end, end: r.end });
                outside.push(Range { start: self.start + 1, end: self.end });
            } else if r.start == self.end {
                // []
                //  ()
                inside.push(Range { start: r.start, end: r.start });
                outside.push(Range { start: self.start, end: self.end - 1 })
            } else if r.start < self.start && r.end == self.end {
                inside.push(self.clone());
            } else if r.start == self.start && r.end == self.end {
                inside.push(self.clone());
            } else if r.start == self.start && r.end < self.end {
                inside.push(r.clone());
                outside.push(Range { start: r.end + 1, end: self.end })
            } else if r.start == self.start && self.end < r.end {
                inside.push(self.clone());
            } else if self.start < r.start && r.end == self.end {
                inside.push(r.clone());
                outside.push(Range { start: self.start, end: r.start - 1 })
            } else {
                println!("{} {}", r.start > self.start, r.end == self.end);
                panic!("{self} {r}");
            }
        }

        return (
            inside.iter().filter(|x| { x.start <= x.end }).cloned().collect::<Vec<Range>>(),
            outside.iter().filter(|x| x.start <= x.end).cloned().collect::<Vec<Range>>()
        );
    }
}

fn pair1() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let groups = content.split("\n\n").collect::<Vec<&str>>();

    let mut maps: Vec<Vec<MapEntry>> = vec![];

    for map in &groups[1..] {
        let map_entries_strs = map[map.find(" map:").unwrap() + 6..]
            .split("\n")
            .collect::<Vec<&str>>();
        let entries = map_entries_strs
            .iter()
            .map(|x| {
                let nums = x
                    .split(" ")
                    .map(|y| i64::from_str(y).unwrap())
                    .collect::<Vec<i64>>();
                return MapEntry {
                    dst_start: nums[0],
                    src_start: nums[1],
                    len: nums[2],
                };
            })
            .collect::<Vec<MapEntry>>();
        maps.push(entries);
    }

    // println!("{:?}", maps);

    let seeds = groups.get(0).unwrap()[7..]
        .split(" ")
        .map(|x| i64::from_str(x).unwrap())
        .collect::<Vec<i64>>();
    let mut smallest_loc = i64::MAX;
    for seed in seeds {
        // println!("\n{}", seed);
        let mut current = seed.clone();
        for map in maps.iter() {
            // println!("-------------------");
            for entry in map.iter() {
                if entry.src_start <= current && current < entry.src_start + entry.len {
                    current = entry.dst_start + (current - entry.src_start);
                    // println!("{:?} -> {current}", entry);
                    break;
                }
            }
        }
        smallest_loc = min(current, smallest_loc);
    }

    println!("{}", smallest_loc)
}

fn part2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let groups = content.split("\n\n").collect::<Vec<&str>>();

    let mut maps: Vec<Vec<MapEntry>> = vec![];

    for map in &groups[1..] {
        let map_entries_strs = map[map.find(" map:").unwrap() + 6..]
            .split("\n")
            .collect::<Vec<&str>>();
        let entries = map_entries_strs
            .iter()
            .map(|x| {
                let nums = x
                    .split(" ")
                    .map(|y| i64::from_str(y).unwrap())
                    .collect::<Vec<i64>>();
                return MapEntry {
                    dst_start: nums[0],
                    src_start: nums[1],
                    len: nums[2],
                };
            })
            .collect::<Vec<MapEntry>>();
        maps.push(entries);
    }

    let seeds = groups.get(0).unwrap()[7..]
        .split(" ")
        .map(|x| i64::from_str(x).unwrap())
        .collect::<Vec<i64>>();
    let mut smallest_loc = i64::MAX;
    for (i, start) in seeds.iter().enumerate() {
        if i % 2 == 1 {
            continue;
        }
        let len = seeds[i + 1];

        let mut current_ranges = vec![Range{start: *start, end: start + len}];

        // for every mapping in maps split all the current ranges and generate dst_ranges
        // the answer is the smallest left bound of all the ranges in the current list

        for map in &maps {
            
            let mut new_out_ranges = vec![];
            let mut new_in_ranges = vec![];

            for entry in map.iter() {
                let r = Range { start: entry.src_start, end: entry.src_start + entry.len - 1 };
                
                for range in current_ranges {
                    let (inside, mut outside) = range.split(r.clone());
                   
                    new_out_ranges.append(&mut outside);
                    for i in &inside {
                        let ri = Range{
                            start: i.start + entry.dst_start - entry.src_start,
                            end: i.end + entry.dst_start - entry.src_start
                        };
                        new_in_ranges.push(ri)
                    }
                }

                current_ranges = vec![];
                current_ranges.append(&mut new_out_ranges);
            }

            current_ranges.append(&mut new_in_ranges);

        }

        for r in current_ranges {
            smallest_loc = min(smallest_loc, r.start);
        }
    }


    println!("{}", smallest_loc)
}

fn main() {
    pair1();
    part2();
}
