use std::{
    collections::{HashMap, HashSet},
    fs::File,
    io::{BufRead, BufReader},
};

#[derive(Debug)]
struct Coords {
    x: i64,
    y: i64,
    z: i64,
}

fn are_boxes_connected(i: usize, j: usize, edges: &HashMap<usize, HashSet<usize>>) -> bool {
    let mut visited = HashSet::new();
    let mut stack = vec![];
    stack.push(i);
    while !stack.is_empty() {
        let j_ = stack.pop().unwrap();
        if visited.contains(&j_) { continue; }
        visited.insert(j_);
        if j_ == j {
            return true;
        }
        if !edges.contains_key(&j_) {
            continue;
        }
        for neigh in &edges[&j_] {
            stack.push(*neigh);
        }
    }

    return false;
}

fn compute_circuit_sizes(boxes: &Vec<Coords>, edges: &HashMap<usize, HashSet<usize>>) -> Vec<i128> {
    let mut visited = HashSet::new();
    let mut circuit_sizes = vec![];

    for i in 0..boxes.len() {
        if visited.contains(&i) {
            continue;
        }
        visited.insert(i);

        let mut boxes = 0;

        let mut stack = vec![];
        stack.push(i);
        while !stack.is_empty() {
            let curr = stack.pop().unwrap();
            visited.insert(curr);
            // println!("{:?}", curr);
            boxes += 1;
            if !edges.contains_key(&curr) {
                continue;
            }
            for neigh in &edges[&curr] {
                if visited.contains(&neigh) || stack.contains(&neigh) {
                    continue;
                }
                stack.push(*neigh);
            }
        }
        // println!("---- {boxes}");
        circuit_sizes.push(boxes);
    }

    return circuit_sizes;
}

fn part1() {
    let target_edge_count = 1000; // for in0 this value was 10
    let file = File::open("in").unwrap();
    let reader = BufReader::new(file);

    let mut boxes = vec![];

    for line in reader.lines().map(|l| l.unwrap()) {
        let coords = line
            .split(",")
            .map(|tok| tok.to_string().parse::<i64>().unwrap())
            .collect::<Vec<i64>>();
        boxes.push(Coords {
            x: coords[0],
            y: coords[1],
            z: coords[2],
        });
    }

    // compute all distances and store them in a vector
    let mut all_distances = vec![];
    for (i, coordsi) in boxes.iter().enumerate() {
        for (j, coordsj) in boxes.iter().enumerate() {
            if i >= j {
                continue;
            }
            let distance = (coordsi.x - coordsj.x).pow(2)
                + (coordsi.y - coordsj.y).pow(2)
                + (coordsi.z - coordsj.z).pow(2);
            all_distances.push((distance, i, j));
        }
    }

    let mut edges: HashMap<usize, HashSet<usize>> = HashMap::new();

    // sort distances
    all_distances.sort();

    // println!("{:?}", all_distances);

    // for distances in ascending order add edges between i and j
    let mut edges_count = 0;
    all_distances.iter().for_each(|(d, i, j)| {
        if edges_count == target_edge_count {
            return;
        };

        if are_boxes_connected(*i, *j, &edges) {
            // println!("{:?} {:?} | {i} -> {j} | {d} - already connected", boxes[*i], boxes[*j]);
            // when i and j are already connected the author assumed we should pretend the wire was used instead of just skipping this edge
            edges_count += 1;
            return;
        }

        // println!("{:?} {:?} | {i} -> {j} | {d}", boxes[*i], boxes[*j]);

        for (i_, j_) in vec![(i, j), (j, i)] {
            if !edges.contains_key(i_) {
                edges.insert(*i_, HashSet::new());
            }
            let list = edges.get_mut(i_).unwrap();
            list.insert(*j_);
        }
        edges_count += 1;
    });

    // traverse the graph and count how many nodes are present in each component
    let mut circuit_sizes = compute_circuit_sizes(&boxes, &edges);

    // multiply the 3 largest component node counts
    let mut result: i128 = 1;
    circuit_sizes.sort_by(|a, b| b.cmp(&a));
    // println!("{:?}", circuit_sizes);
    for val in &circuit_sizes[..3] {
        result *= val;
    }
    println!("Part 1 answer: {:?}", result);
}




fn part2() {
    let file = File::open("in").unwrap();
    let reader = BufReader::new(file);

    let mut boxes = vec![];

    for line in reader.lines().map(|l| l.unwrap()) {
        let coords = line
            .split(",")
            .map(|tok| tok.to_string().parse::<i64>().unwrap())
            .collect::<Vec<i64>>();
        boxes.push(Coords {
            x: coords[0],
            y: coords[1],
            z: coords[2],
        });
    }

    // compute all distances and store them in a vector
    let mut all_distances = vec![];
    for (i, coordsi) in boxes.iter().enumerate() {
        for (j, coordsj) in boxes.iter().enumerate() {
            if i >= j {
                continue;
            }
            let distance = (coordsi.x - coordsj.x).pow(2)
                + (coordsi.y - coordsj.y).pow(2)
                + (coordsi.z - coordsj.z).pow(2);
            all_distances.push((distance, i, j));
        }
    }

    let mut edges: HashMap<usize, HashSet<usize>> = HashMap::new();

    // sort distances
    all_distances.sort();

    // println!("{:?}", all_distances);

    let mut should_stop_adding_edges = false;

    let mut result: i64 = 1;

    // for distances in ascending order add edges between i and j
    all_distances.iter().for_each(|(d, i, j)| {
        if should_stop_adding_edges {
            return;
        };

        if are_boxes_connected(*i, *j, &edges) {
            // println!("{:?} {:?} | {i} -> {j} | {d} - already connected", boxes[*i], boxes[*j]);
            // when i and j are already connected the author assumed we should pretend the wire was used instead of just skipping this edge
            return;
        }

        // println!("{:?} {:?} | {i} -> {j} | {d}", boxes[*i], boxes[*j]);

        for (i_, j_) in vec![(i, j), (j, i)] {
            if !edges.contains_key(i_) {
                edges.insert(*i_, HashSet::new());
            }
            let list = edges.get_mut(i_).unwrap();
            list.insert(*j_);
        }

        // traverse the graph and count how many nodes are present in each component
        let circuit_sizes = compute_circuit_sizes(&boxes, &edges);
        if circuit_sizes.len() == 1 {
            should_stop_adding_edges = true;
            result = boxes[*i].x * boxes[*j].x;
        }
    });

   
    println!("Part 1 answer: {:?}", result);
}


fn main() {
    // part1();
    part2();
}
