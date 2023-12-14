use std::fs;

fn solution(dist: i128) {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();
    // println!("{:?}", lines);

    let mut galaxies = Vec::new();


    let mut does_col_have_galaxies = vec![];
    let mut does_line_have_galaxies = vec![];

    for _ in 0..lines.len() {
        does_line_have_galaxies.push(false);
    }

    for _ in 0..lines[0].len() {
        does_col_have_galaxies.push(false);
    }


    for (i, line) in lines.iter().enumerate() {
        for (j, ch) in line.chars().enumerate() {
            if ch == '#' {
                galaxies.push((i, j));
                does_line_have_galaxies[i] = true;
                does_col_have_galaxies[j] = true;
            }
        }
    }


    let mut sums = 0;

    for i in 0..galaxies.len() {
        for j in i + 1..galaxies.len() {
            let (x1, y1) = galaxies[i];
            let (x2, y2) = galaxies[j];
            let mut sum = 0;
            // x1.abs_diff(x2) + y1.abs_diff(y2);

            let (minx, maxx) = (x1.min(x2), x1.max(x2));
            for idx in minx..maxx {
                if does_line_have_galaxies[idx] {
                    sum += 1;
                } else {
                    sum += dist;
                }
            }

            let (miny, maxy) = (y1.min(y2), y1.max(y2));
            for idx in miny..maxy {
                if does_col_have_galaxies[idx] {
                    sum += 1;
                } else {
                    sum += dist;
                }
            }

            sums += sum;
        }
    }

    // println!("{:?}", galaxies);
    println!("{:?}", sums);

}


fn main() {
    solution(2);
    solution(1000000);
}



// ....1........
// .........2...
// 3............
// .............
// .............
// ........4....
// .5...........
// .##.........6
// ..##.........
// ...##........
// ....##...7...
// 8....9.......

// This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

// Between galaxy 1 and galaxy 7: 15
// Between galaxy 3 and galaxy 6: 17
// Between galaxy 8 and galaxy 9: 5
// In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.