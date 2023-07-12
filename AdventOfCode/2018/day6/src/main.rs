
use std::fs;
use std::ops::Add;

fn manhattan(p1: Vec<i32>, p2: Vec<i32>) -> i32 {
    return (p1[0] - p2[0]).abs() + (p1[1] - p2[1]).abs();
}

fn p1() {
    let contents = fs::read_to_string("input")
        .expect("File contents should be read here");

    let mut coords: Vec<Vec<i32>> = Vec::new();
    let mut bounds: Vec<i32> =vec![0, 0];

    for line in contents.split("\n") {
        let coords_: Vec<i32> = line
            .split(", ")
            .map(|x| x.trim().parse().expect("String is not an integer"))
            .collect();
        assert_eq!(coords_.len(), 2);
        bounds[0] = bounds[0].max(coords_[0] * 2);
        bounds[1] = bounds[1].max(coords_[1] * 2);
        coords.push(coords_);
    }

    let mut map_idx: Vec<Vec<i32>> = Vec::new();
    let mut map_val: Vec<Vec<i32>> = Vec::new();
    map_idx.resize(bounds[1] as usize, vec![-1; bounds[0] as usize]);
    map_val.resize(bounds[1] as usize, vec![i32::MAX; bounds[0] as usize]);


    let mut count: Vec<i32> = vec![0; coords.len()];

    for (k, xy) in coords.iter().enumerate() {
        for (i, row) in map_val.clone().iter().enumerate() {
            for (j, elem) in row.iter().enumerate() {
                let new_dist = manhattan(xy.clone(), vec![i as i32, j as i32]);
                if new_dist < *elem {
                    if map_idx[i][j] != -1 {
                        count[map_idx[i][j] as usize] -= 1;
                    }
                    map_val[i][j] = new_dist;
                    map_idx[i][j] = k as i32;
                    count[k] += 1;
                } else if new_dist == *elem {
                    if map_idx[i][j] != -1 {
                        count[map_idx[i][j] as usize] -= 1;
                    }
                    map_idx[i][j] = -1;
                }
            }
        }
    }

    for val in &map_idx[0] {
        if *val != -1 {
            count[*val as usize] = -1;
        }
    }

    for val in &map_idx[map_idx.len() - 1] {
        if *val != -1 {
            count[*val as usize] = -1;
        }
    }

    for row in &map_idx {
        let mut val = row[0];
        if val != -1 {
            count[val as usize] = -1;
        }
        val = row[row.len() - 1];
        if val != -1 {
            count[val as usize] = -1;
        }
    }


    let mut max_val = 0;
    for val in count {
        print!("{} ", val);
        max_val = max_val.max(val)
    }
    println!();
    println!("max: {}", max_val);

    // for row in map_val {
    //     for val in row {
    //         print!("{} ", val);
    //     }
    //     println!();
    // }
    // println!();

    for row in &map_idx {
        for val in row {
            if *val == -1 {
                print!(". ");
            } else {
                print!("{} ", char::from_u32('A' as u32 + *val as u32).unwrap());
            }
        }
        println!();
    }
    println!();

    // for (i, row) in map_idx.iter().enumerate() {
    //     for (j, _) in row.iter().enumerate() {
    //         let mut coord_idx: i32 = -1;
    //         for (k, coord) in coords.iter().enumerate() {
    //             if coord[0] == i as i32 && coord[1] == j as i32 {
    //                 coord_idx = k as i32;
    //             }
    //         }
    //
    //         if coord_idx == -1 {
    //             print!(". ");
    //         } else {
    //             print!("{} ", char::from_u32('A' as u32 + coord_idx as u32).unwrap());
    //         }
    //     }
    //     println!();
    // }
}


fn p2() {
    let contents = fs::read_to_string("input")
        .expect("File contents should be read here");

    let mut coords: Vec<Vec<i32>> = Vec::new();
    let mut bounds: Vec<i32> =vec![0, 0];

    for line in contents.split("\n") {
        let coords_: Vec<i32> = line
            .split(", ")
            .map(|x| x.trim().parse().expect("String is not an integer"))
            .collect();
        assert_eq!(coords_.len(), 2);
        bounds[0] = bounds[0].max(coords_[0]);
        bounds[1] = bounds[1].max(coords_[1]);
        coords.push(coords_);
    }

    let mut in_region = 0;
    for i in 0..bounds[0] {
        for j in 0..bounds[1] {
            let sum: i32 = coords.iter().map(|x| manhattan(vec![x[0], x[1]], vec![i, j])).sum();
            if sum < 10000 {
                in_region = in_region.add(1);
            }
        }
    }
    println!("in_region {}", in_region)
}

fn main() {
    // p1();
    p2();
}