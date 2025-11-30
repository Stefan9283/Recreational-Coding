use std::hash::Hash;
use std::{
    collections::{HashSet, VecDeque},
    fs,
};

#[derive(Debug, Hash, PartialEq, Eq, Clone, Copy)]
enum Direction {
    UP,
    DOWN,
    LEFT,
    RIGHT,
}

#[derive(Debug, Hash, PartialEq, Eq, Clone, Copy)]
struct RaySource {
    dir: Direction,
    position: (i32, i32),
}

fn get_first_mirror(
    ray: &RaySource,
    map: &Vec<Vec<char>>,
    visited: &mut HashSet<(i32, i32)>,
) -> Option<(i32, i32)> {
    match ray.dir {
        Direction::UP => {
            for i in (0..ray.position.0).rev() {
                visited.insert((i, ray.position.1));
                if map[i as usize][ray.position.1 as usize] != '.' {
                    return Some((i as i32, ray.position.1));
                }
            }
        }
        Direction::DOWN => {
            for i in ray.position.0 + 1..map.len() as i32 {
                visited.insert((i, ray.position.1));
                if map[i as usize][ray.position.1 as usize] != '.' {
                    return Some((i as i32, ray.position.1));
                }
            }
        }
        Direction::LEFT => {
            for i in (0..ray.position.1).rev() {
                visited.insert((ray.position.0, i));
                if map[ray.position.0 as usize][i as usize] != '.' {
                    return Some((ray.position.0, i as i32));
                }
            }
        }
        Direction::RIGHT => {
            for i in ray.position.1 + 1..map[0].len() as i32 {
                visited.insert((ray.position.0, i));
                if map[ray.position.0 as usize][i as usize] != '.' {
                    return Some((ray.position.0, i as i32));
                }
            }
        }
    }

    return None;
}

fn get_energized_count(input_file: &str, initial_ray: RaySource) -> i32 {
    let content = fs::read_to_string(input_file).expect("Should be able to read the input from file");

    let lines = content
        .split("\n")
        .map(|x| x.chars().collect())
        .collect::<Vec<Vec<char>>>();

    let mut stack = VecDeque::new();
    stack.push_back(initial_ray);
    let mut visited = HashSet::new();
    let mut energized = HashSet::new();
    while !stack.is_empty() {
        let ray = stack.pop_front().unwrap();
        if visited.contains(&ray.clone()) {
            continue;
        }
        visited.insert(ray.clone());
        energized.insert(ray.position.clone());
        // println!("{:?}", ray);

        match get_first_mirror(&ray, &lines, &mut energized) {
            Some(pos) => {
                let c = lines[pos.0 as usize][pos.1 as usize];
                // println!("\tmirror at {:?} {c}", pos);
                if c == '|' {
                    if matches!(ray.dir, Direction::LEFT) || matches!(ray.dir, Direction::RIGHT) {
                        // split into 2 rays
                        stack.push_back(RaySource {
                            dir: Direction::DOWN,
                            position: pos,
                        });
                        stack.push_back(RaySource {
                            dir: Direction::UP,
                            position: pos,
                        });
                    } else {
                        // go through
                        match ray.dir {
                            Direction::UP => {
                                stack.push_back(RaySource {
                                    dir: Direction::UP,
                                    position: pos,
                                });
                            }
                            Direction::DOWN => {
                                stack.push_back(RaySource {
                                    dir: Direction::DOWN,
                                    position: pos,
                                });
                            }
                            _ => {}
                        }
                    }
                } else if c == '-' {
                    if matches!(ray.dir, Direction::UP) || matches!(ray.dir, Direction::DOWN) {
                        // split into 2 rays
                        stack.push_back(RaySource {
                            dir: Direction::LEFT,
                            position: pos,
                        });
                        stack.push_back(RaySource {
                            dir: Direction::RIGHT,
                            position: pos,
                        });
                    } else {
                        // go through
                        match ray.dir {
                            Direction::LEFT => {
                                stack.push_back(RaySource {
                                    dir: Direction::LEFT,
                                    position: pos,
                                });
                            }
                            Direction::RIGHT => {
                                stack.push_back(RaySource {
                                    dir: Direction::RIGHT,
                                    position: pos,
                                });
                            }
                            _ => {}
                        }
                    }
                } else if c == '/' {
                    match ray.dir {
                        Direction::UP => {
                            // right
                            stack.push_back(RaySource {
                                dir: Direction::RIGHT,
                                position: pos,
                            });
                        }
                        Direction::DOWN => {
                            // left
                            stack.push_back(RaySource {
                                dir: Direction::LEFT,
                                position: pos,
                            });
                        }
                        Direction::LEFT => {
                            // down
                            stack.push_back(RaySource {
                                dir: Direction::DOWN,
                                position: pos,
                            });
                        }
                        Direction::RIGHT => {
                            // up
                            stack.push_back(RaySource {
                                dir: Direction::UP,
                                position: pos,
                            });
                        }
                    }
                } else if c == '\\' {
                    match ray.dir {
                        Direction::UP => {
                            // left
                            stack.push_back(RaySource {
                                dir: Direction::LEFT,
                                position: pos,
                            });
                        }
                        Direction::DOWN => {
                            // right
                            stack.push_back(RaySource {
                                dir: Direction::RIGHT,
                                position: pos,
                            });
                        }
                        Direction::LEFT => {
                            // up
                            stack.push_back(RaySource {
                                dir: Direction::UP,
                                position: pos,
                            });
                        }
                        Direction::RIGHT => {
                            // down
                            stack.push_back(RaySource {
                                dir: Direction::DOWN,
                                position: pos,
                            });
                        }
                    }
                }
            }
            None => {}
        }

        /*
        If the beam encounters empty space (.), it continues in the same direction.
        If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending
            on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror
            would continue upward in the mirror's column, while a rightward-moving beam that
            encounters a \ mirror would continue downward from the mirror's column.
        If the beam encounters the pointy end of a splitter (| or -), the beam passes through
            the splitter as if the splitter were empty space. For instance, a rightward-moving beam
            that encounters a - splitter would continue in the same direction.
        If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams
            going in each of the two directions the splitter's pointy ends are pointing. For instance,
            a rightward-moving beam that encounters a | splitter would split into two beams: one that
            continues upward from the splitter's column and one that continues downward from the splitter's column.
         */
    }
    // println!("energized {:?} {}", energized, energized.len() - 1);
    return energized.len() as i32 - 1;
}

fn main() {
    let input = "in";
    {
        let res = get_energized_count(input, RaySource {
            dir: Direction::RIGHT,
            position: (0, -1),
        });
        println!("part1: {res}")
    }
    {
        let mut max_e = 0;
        let content = fs::read_to_string(input).unwrap();
        let lines = content.split("\n").collect::<Vec<&str>>();
        let (h, w) = (lines.len(), lines[0].len());
        for i in 0..h {
            let e1 = get_energized_count(input, RaySource { dir: Direction::RIGHT, position: (i as i32, -1) });
            let e2 = get_energized_count(input, RaySource { dir: Direction::LEFT, position: (i as i32, w as i32) });
            max_e = max_e.max(e1.max(e2));
            // println!("w {:?}={e1} {:?}={e2}", (i, 0), (i, w));
        }
        for i in 0..w {
            let e1 = get_energized_count(input, RaySource { dir: Direction::DOWN, position: (-1, i as i32) });
            let e2 = get_energized_count(input, RaySource { dir: Direction::UP, position: (h as i32, i as i32) });
            max_e = max_e.max(e1.max(e2));
            // println!("w {:?}={e1} {:?}={e2}", (0, i), (h, i));
        }
        println!("part2: {max_e}")
    }
}
