use core::time;
use std::{collections::{HashMap, HashSet}, fs::File, io::{BufRead, BufReader}};

#[allow(dead_code)]
fn part1() {
    let file = File::open("in").expect("file should exist");
    let reader = BufReader::new(file);

    let mut map= vec![];

    for line in reader.lines() {
        // let row = line.unwrap().chars().collect::<Vec<char>>();
        // map.push(row);
        map.push(line.unwrap());
    }

    map[0] = map[0].replace("S", "|");
    
    let mut split_counter = 0;

    let mut current_idx = 0;

    while current_idx < map.len() - 1 {
        let mut row_below = map[current_idx+1].chars().collect::<Vec<char>>();
        
        for (i, c) in map[current_idx].chars().enumerate() {
            if c != '|' { continue; }


            // ray propagation
            match row_below[i] {
                '.' => {row_below[i] = '|' }
                '^' => {
                    split_counter += 1;
                    if i != 0 { row_below[i-1] = '|' }
                    if i != map[0].len()-1 { row_below[i+1] = '|' }
                },
                _ => {}
            }
        } 


        map[current_idx+1] = row_below.iter().map(|x| { return x.to_string() }).collect::<Vec<String>>().join("");

        current_idx += 1;
    }


    println!("{:?}", map);
    println!("Part 1 answer: {split_counter}");

}

#[allow(dead_code)]
fn split_timeline(mut map: Vec<String>, init_row: usize, timelines_set: &mut HashSet<String>) {

    let mut current_idx = init_row;

    while current_idx < map.len() - 1 {
        // println!("curr row {current_idx}");

        let mut row_below = map[current_idx+1].chars().collect::<Vec<char>>();
        
        for (i, c) in map.clone()[current_idx].chars().enumerate() {
            if c != '|' { continue; }

            // ray propagation
            match row_below[i] {
                '.' => {
                    row_below[i] = '|';
                    map[current_idx+1] = row_below.iter().map(|x| { return x.to_string() }).collect::<Vec<String>>().join("");
                }
                _ => {}
            }
        } 

        // for line in &map {
        //     println!("{:?}", line)
        // }

        for (i, c) in map.clone()[current_idx].chars().enumerate() {
            if c != '|' { continue; }
            
            // ray splits
            match row_below[i] {
                '^' => {
                    if i != 0 && row_below[i-1] == '.' {
                        let mut map_left = map.clone();
                        let mut row_below_left = row_below.clone();
                        row_below_left[i-1] = '|';
                        map_left[current_idx+1] = row_below_left.iter().map(|x| { return x.to_string() }).collect::<Vec<String>>().join("");
                        // println!("split l {} {}", current_idx+1, i-1);
                        split_timeline(map_left, current_idx+1, timelines_set);
                    }
                    if i != map[0].len()-1 && row_below[i+1] == '.' {
                        let mut map_right = map.clone();
                        let mut row_below_right = row_below.clone();
                        row_below_right[i+1] = '|';
                        map_right[current_idx+1] = row_below_right.iter().map(|x| { return x.to_string() }).collect::<Vec<String>>().join("");
                        // println!("split r {} {}", current_idx+1, i+1);
                        split_timeline(map_right, current_idx+1, timelines_set);
                    }
                    return;
                },
                _ => {}
            }
        }

        current_idx += 1;
    }

    timelines_set.insert(map.join("\n"));
}

#[allow(dead_code)]
fn split_timeline_iterative(init_map: Vec<String>) -> usize {
    // let mut timeline_set = HashSet::new(); 

    let mut stack = vec![];
    stack.push((init_map, 0));

    let mut counter = 0;

    while !stack.is_empty() {
        
        println!("{}", stack.len());

        let (mut map, row) = stack.pop().unwrap();   

        {
            println!("{} {row}", map.join("\n"))
        }

        if row == map.len() - 1 {
            // timeline_set.insert(map.join("\n"));
            counter += 1;
            continue;
        }


        let mut row_below = map[row+1].chars().collect::<Vec<char>>();

        for (i, c) in map.clone()[row].chars().enumerate() {
            if c != '|' { continue; }

            // ray propagation
            match row_below[i] {
                '.' => {
                    row_below[i] = '|';
                    map[row+1] = row_below.iter().map(|x| { return x.to_string() }).collect::<Vec<String>>().join("");
                }
                _ => {}
            }
        }

        let mut split = false;
        for (i, c) in map.clone()[row].chars().enumerate() {
            if c != '|' { continue; }
            
            
            // ray splits
            match row_below[i] {
                '^' => {
                    split = true;
                    if i != 0 && row_below[i-1] == '.' {
                        let mut map_left = map.clone();
                        let mut row_below_left = row_below.clone();
                        row_below_left[i-1] = '|';
                        map_left[row+1] = row_below_left.iter().map(|x| { return x.to_string() }).collect::<Vec<String>>().join("");
                        stack.push((map_left, row+1));
                    }
                    if i != map[0].len()-1 && row_below[i+1] == '.' {
                        let mut map_right = map.clone();
                        let mut row_below_right = row_below.clone();
                        row_below_right[i+1] = '|';
                        map_right[row+1] = row_below_right.iter().map(|x| { return x.to_string() }).collect::<Vec<String>>().join("");
                        stack.push((map_right, row+1));
                    }
                },
                _ => {}
            }

            if !split {
                stack.push((map.clone(), row+1));
            }
        }
    }

    return counter;
    // return timeline_set.len();
}

#[allow(dead_code)]
#[derive(Debug)]
struct Edge {
    left: Option<(usize, usize)>,
    right: Option<(usize, usize)>
}

fn count_timelines(map: Vec<String>) -> i64 {

    let mut edges: HashMap<(usize, usize), Edge> = HashMap::new();
    let mut timelines_from_node: HashMap<(usize, usize), i64> = HashMap::new();

    let (s_idx, _) = map[0].char_indices().find(|(_idx, ch)| { 
        return *ch == 'S'
    }).unwrap();

    let mut stack = vec![];

    let mut fst_splitter: (usize, usize) = (0, 0);

    {
        // find the first spliter
        for i in 0..map.len() {
            let ret = map[i].char_indices().find(|(_, ch)| {
                return *ch == '^';
            });
            match ret {
                Some((_, _)) => {
                    fst_splitter = (i, s_idx);
                    stack.push(fst_splitter);
                    break;
                },
                None => {}
            }
        }
    }

    {
        // recursively for each spliter find the next spliter on left and right and create entires in edges and timelines_from_node (init this one with 0)
        while !stack.is_empty() {
            let (i, j) = stack.pop().unwrap();

            let next = vec![(i + 1, j-1), (i + 1, j+1)].iter().map(|(x, y)| {
                for i in (*x + 1)..map.len() {
                    let ret = map[i].char_indices().find(|(idx, ch)| {
                        return *ch == '^' && y == idx;
                    });
                    match ret {
                        Some((_, _)) => {
                            return Some((i, *y));
                        },
                        None => {}
                    }
                }
                return None;
            }).collect::<Vec<Option<(usize, usize)>>>();

            // println!("{:?} -> {:?}", (i, j), next);

            edges.insert((i, j), Edge { left: next[0], right: next[1] });
            timelines_from_node.insert((i, j),  0);

            next.iter().filter(|x| x.is_some()).for_each(|x| {
                let coords = x.unwrap();
                if !timelines_from_node.contains_key(&coords) {
                    stack.push(coords);
                }
            });
        }
    }

    // println!("{:?} {:?}", edges, timelines_from_node);

    {
        let mut stack = vec![];
        edges.iter().for_each(|x| {
            stack.push(*x.0);
        });

        let mut visited: HashSet<(usize, usize)> = HashSet::new();

        while !stack.is_empty() {
            let (i, j) = stack.pop().unwrap();

            let edge = &edges[&(i, j)];
            
            let mut can_compute = true;


            for next in vec![edge.left, edge.right] {
                match next {
                    Some(coords) => {
                        if !visited.contains(&coords) {
                            can_compute = false;
                        }
                    },
                    None => {},
                }
            }


            if !can_compute { 
                stack.insert(0, (i, j));
                continue; 
            }


            visited.insert((i, j));
            
            // println!("{:?} {:?}", (i, j), edge);

            for next in vec![edge.left, edge.right] {
                match next {
                    Some(coords) => {
                        let child_branches = timelines_from_node[&coords];
                        // println!("{:?} {:?}", coords, child_branches);
                        timelines_from_node.insert((i, j), timelines_from_node[&(i, j)] + child_branches);
                    },
                    None => {
                        timelines_from_node.insert((i, j), timelines_from_node[&(i, j)] + 1);
                        // println!("{:?} {:?}", next, timelines_from_node[&(i, j)]);
                    },
                }
            }
        }

        // let mut keys: Vec<(usize, usize)> = timelines_from_node.keys().into_iter().map(|x| *x).collect();
        // keys.sort_by(|a,b| {
        //     if a.0 != b.0 {
        //         return b.cmp(a)
        //     }
        //     return a.1.cmp(&b.1);
        // });

        // for k in keys {
        //     println!("{:?} {}", k, timelines_from_node[&k])
        // }

    }

    return timelines_from_node[&fst_splitter];
}


fn part2() {
    let file = File::open("in").expect("file should exist");
    let reader = BufReader::new(file);

    let mut map= vec![];

    for line in reader.lines() {
        // let row = line.unwrap().chars().collect::<Vec<char>>();
        // map.push(row);
        map.push(line.unwrap());
    }

    // map[0] = map[0].replace("S", "|");

    // attempt 1
    // let timeline_set = &mut HashSet::new(); 
    // split_timeline(map.clone(), 0, timeline_set);
    // println!("Part 2 answer: {}", timeline_set.len());

    // attempt 2
    // println!("Part 2 answer: {}", split_timeline_iterative(map));

    // attempt 3
    println!("Part 2 answer: {}", count_timelines(map));

}


fn main() {
    // part1()
    part2()
}
