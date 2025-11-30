use std::fs;
use std::str::FromStr;

enum Part {
    Part1,
    Part2,
}

fn orientation(src: (i32, i32), dst: (i32, i32)) -> char {
    if src.0 == dst.0 {
        return 'O';
    }
    if src.1 == dst.1 {
        return 'V';
    }
    return '?';
}

fn is_on_line(src: (i32, i32), dst: (i32, i32), o: (i32, i32)) -> bool {
    let h1   = f32::sqrt(((o.0   - src.0).pow(2) + (o.1   - src.1).pow(2)) as f32) as i32;
    let h2   = f32::sqrt(((o.0   - dst.0).pow(2) + (o.1   - dst.1).pow(2)) as f32) as i32;
    let line = f32::sqrt(((dst.0 - src.0).pow(2) + (dst.1 - src.1).pow(2)) as f32) as i32;

    // println!("{:?}", (h1, h2, line));

    h1 + h2 == line
}

// split segment (src1, dst1) by line (src2, dst2)
fn intersect(
    src1: (i32, i32),
    dst1: (i32, i32),
    src2: (i32, i32),
    dst2: (i32, i32),
) -> Option<(i32, i32)> {
    println!("\nAAAA {:?}", (src1, dst1, src2, dst2));

    let src1_ = (src1.0.min(dst1.0), src1.1.min(dst1.1));
    let dst1_ = (src1.0.max(dst1.0), src1.1.max(dst1.1));
    let src2_ = (src2.0.min(dst2.0), src2.1.min(dst2.1));
    let dst2_ = (src2.0.max(dst2.0), src2.1.max(dst2.1));

    println!("BBBB {:?}", (src1_, dst1_, src2_, dst2_));

    if orientation(src1_, dst1_) == orientation(src2_, dst2_) {
        return None;
    }

    let (x1, y1) = src1_;
    let (x2, y2) = dst1_;
    let (x3, y3) = src2_;
    let (x4, y4) = dst2_;

    let px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4))
        / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4));
    let py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4))
        / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4));

    if is_on_line(src1_, dst1_, (px, py)) && is_on_line(src2_, dst2_, (px, py)) {
        println!("{:?}", (px, py));
        return Some((px, py));
    } 

    return None;
}

fn main() {
    let part = Part::Part1;
    let content = fs::read_to_string("in0").unwrap();

    let mut pool: Vec<((i32, i32), (i32, i32))> = vec![];

    let mut current_pos = (0, 0);
    // pool.add_node(current_pos);
    for line in content.split("\n") {
        let tokens = line.split(" ").collect::<Vec<&str>>();
        // println!("{:?}", tokens);
        // println!("{:?}", current_pos);
        let src = current_pos.clone();
        match part {
            Part::Part1 => {
                let steps = i32::from_str(tokens[1]).unwrap();
                let dir = tokens[0];
                if dir == "U" {
                    current_pos.1 += steps;
                }
                if dir == "D" {
                    current_pos.1 -= steps;
                }
                if dir == "L" {
                    current_pos.0 -= steps;
                }
                if dir == "R" {
                    current_pos.0 += steps;
                }
            }
            Part::Part2 => {
                let steps = i32::from_str_radix(&tokens[2][2..7], 16).unwrap();
                let dir = &tokens[2][7..8];
                // println!("{:?}", (steps, dir));
                if dir == "3" {
                    current_pos.1 += steps;
                }
                if dir == "1" {
                    current_pos.1 -= steps;
                }
                if dir == "2" {
                    current_pos.0 -= steps;
                }
                if dir == "0" {
                    current_pos.0 += steps;
                }
            }
        };
        // pool.add_node(current_pos);
        pool.push((src, current_pos));
    }
    /*
       Pool {
           vertices: {
                0: {0,            6},
               -2: {0,     2       },
               -5: {0,     2,  4, 6},
               -7: {0, 1,      4, 6},
               -9: {   1,         6},
           }
           edges: {
            (1, -9): {(1, -7), (6, -9)},
            (1, -7): {(0, -7), (1, -9)},
            (2, -2): {(0, -2), (2, -5)},
            (6, -9): {(6, -7), (1, -9)},
            (0, -7): {(1, -7), (0, -5)},
            (4, -5): {(4, -7), (6, -5)},
            (0, -5): {(0, -7), (2, -5)},
            (2, -5): {(0, -5), (2, -2)},
            (0, -2): {(0, 0), (2, -2)},
            (6, -5): {(6, 0), (4, -5)},
            (0, 0): {(6, 0), (0, -2)},
            (6, 0): {(6, -5), (0, 0)},
            (4, -7): {(6, -7), (4, -5)},
            (6, -7): {(4, -7), (6, -9)}

            // BSP ca in Doom?
        }
       }
    */
    println!("{:?}", pool);

    let pool2: Vec<((i32, i32), (i32, i32))> = vec![];

    for e in &pool {
        let intersec = intersect(e.0, e.1, (2, 3), (2, -100));
    }

    println!("{:?}", pool2);
}
