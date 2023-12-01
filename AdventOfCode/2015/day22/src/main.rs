use std::cmp::max;
use std::collections::LinkedList;
use std::fmt::{Debug, Formatter};
use std::fs;
use std::str::FromStr;

#[derive(Debug, Clone, Copy)]
struct Player {
    health: i32,
    armour: i32,
    mana: i32,
}

#[derive(Debug, Clone, Copy)]
struct Enemy {
    health: i32,
    damage: i32,
}

trait Spell {
    fn init(&mut self, player: &mut Player, enemy: &mut Enemy);
    fn cost(&self) -> i32;
    fn update(&mut self, player: &mut Player, enemy: &mut Enemy);
    fn has_timed_out(&mut self) -> bool;
    fn destroy(&mut self, player: &mut Player, enemy: &mut Enemy);
    fn clone_dyn(&self) -> Box<dyn Spell>;

    fn name(&self) -> String;
}

#[derive(Debug, Clone)]
struct MagicMissile;
#[derive(Debug, Clone)]
struct Drain;
#[derive(Debug, Clone)]
struct Shield {
    timeout: i32
}
#[derive(Debug, Clone)]
struct Poison {
    timeout: i32
}
#[derive(Debug, Clone)]
struct Recharge {
    timeout: i32
}

impl Spell for MagicMissile {
    fn init(&mut self, player: &mut Player, enemy: &mut Enemy) {
        player.mana -= self.cost();
        enemy.health -= 4;
    }

    fn cost(&self) -> i32 {
        return 53
    }

    fn update(&mut self, _player: &mut Player, _enemy: &mut Enemy) {}

    fn has_timed_out(&mut self) -> bool { return true; }

    fn destroy(&mut self, _player: &mut Player, _enemy: &mut Enemy) {}

    fn clone_dyn(&self) -> Box<dyn Spell> {
        Box::new(self.clone())
    }

    fn name(&self) -> String {
        "MagicMissile".to_string()
    }
}

impl Spell for Drain {
    fn init(&mut self, player: &mut Player, enemy: &mut Enemy) {
        player.mana -= self.cost();
        player.health += 2;
        enemy.health -= 2;
    }

    fn cost(&self) -> i32 {
        return 73;
    }

    fn update(&mut self, _player: &mut Player, _enemy: &mut Enemy) {}

    fn has_timed_out(&mut self) -> bool {
        return true;
    }

    fn destroy(&mut self, _player: &mut Player, _enemy: &mut Enemy) {}

    fn clone_dyn(&self) -> Box<dyn Spell> {
        Box::new(self.clone())
    }

    fn name(&self) -> String {
        "Drain".to_string()
    }
}

impl Default for Shield {
    fn default() -> Self {
        Self::from(Shield{ timeout: 6 })
    }
}

impl Default for Poison {
    fn default() -> Self {
        Poison{ timeout: 6 }
    }
}

impl Default for Recharge {
    fn default() -> Self {
        Recharge{ timeout: 5 }
    }
}




impl Spell for Shield {
    fn init(&mut self, player: &mut Player, _enemy: &mut Enemy) {
        player.mana -= self.cost();
        player.armour += 7;
    }

    fn cost(&self) -> i32 {
        return 113
    }

    fn update(&mut self, _player: &mut Player, _enemy: &mut Enemy) {
        self.timeout -= 1;
    }

    fn has_timed_out(&mut self) -> bool {
        return self.timeout == 0
    }

    fn destroy(&mut self, player: &mut Player, _enemy: &mut Enemy) {
        player.armour -= 7;
    }

    fn clone_dyn(&self) -> Box<dyn Spell> {
        Box::new(self.clone())
    }

    fn name(&self) -> String {
        "Shield".to_string()
    }
}

impl Spell for Poison {
    fn init(&mut self, player: &mut Player, _enemy: &mut Enemy) {
        player.mana -= self.cost();
        self.timeout = 6;
    }

    fn cost(&self) -> i32 {
        return 173;
    }

    fn update(&mut self, _player: &mut Player, enemy: &mut Enemy) {
        self.timeout -= 1;
        enemy.health -= 3;
    }

    fn has_timed_out(&mut self) -> bool {
        return self.timeout == 0;
    }

    fn destroy(&mut self, _player: &mut Player, _enemy: &mut Enemy) {}

    fn clone_dyn(&self) -> Box<dyn Spell> {
        Box::new(self.clone())
    }

    fn name(&self) -> String {
        "Poison".to_string()
    }
}

impl Spell for Recharge {
    fn init(&mut self, player: &mut Player, _enemy: &mut Enemy) {
        player.mana -= self.cost();
        self.timeout = 5;
    }

    fn cost(&self) -> i32 {
        return 229;
    }

    fn update(&mut self, player: &mut Player, _enemy: &mut Enemy) {
        player.mana += 101;
        self.timeout -= 1;
    }

    fn has_timed_out(&mut self) -> bool {
        return self.timeout == 0;
    }

    fn destroy(&mut self, _player: &mut Player, _enemy: &mut Enemy) {}

    fn clone_dyn(&self) -> Box<dyn Spell> {
        Box::new(self.clone())
    }

    fn name(&self) -> String {
        "Recharge".to_string()
    }
}

impl Clone for Box<dyn Spell> {
    fn clone(&self) -> Self {
        return self.clone_dyn();
    }
}

#[derive(Debug)]
struct GameState {
    player: Player,
    enemy: Enemy,
    active_spells: Vec<Box<dyn Spell>>,
    choices: Vec<String>,
    turn: i32,
    used_mana: i32
}

impl Debug for dyn Spell {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        return f.debug_struct("Spell")
            .field("type", &self.name())
            .finish();
    }
}




fn part1() {

    let content: String = fs::read_to_string("in").expect("Should be able to read from file");
    let lines: Vec<_> = content.split("\n").collect();

    let mut s: LinkedList<GameState> = LinkedList::new();
    s.push_back(GameState{
        player: Player { health: 50, armour: 0, mana: 500 },
        enemy: Enemy {
            health: i32::from_str(lines[0].split(" ").last().expect("There should be at least one token")).expect("Token should be an int"),
            damage: i32::from_str(lines[1].split(" ").last().expect("There should be at least one token")).expect("Token should be an int")
        },
        choices: vec![],
        active_spells: vec![], turn: 0, used_mana: 0});

    let mut min_mana: i32 = i32::MAX;

    while !s.is_empty() {
        let state = s.pop_front().unwrap();

        let mut player = state.player.clone();
        let mut enemy = state.enemy.clone();
        let active_spells = state.active_spells.clone();
        let used_mana = state.used_mana.clone();
        let turn = state.turn.clone();
        let choices = state.choices.clone();

        let mut next_active_spells: Vec<Box<dyn Spell>> = Vec::new();

        if used_mana > min_mana {
            continue;
        }

        // update all spells
        for mut spell in active_spells {
            spell.update(&mut player, &mut enemy);
            if !spell.has_timed_out() {
                next_active_spells.push(spell.clone());
            } else {
                spell.destroy(&mut player, &mut enemy);
            }
        }

        if player.health <= 0 {
            continue;
        } else if enemy.health <= 0 {
            if min_mana > used_mana {
                min_mana = used_mana;
                println!("Win at state: {:?}", state);
                println!("Min mana used {}", used_mana);
            }
        }


        if turn % 2 == 0 {
            let possible_spells: Vec<Box<dyn Spell>> = vec![
                Box::new(MagicMissile),
                Box::new(Drain),
                Box::new(Shield::default()),
                Box::new(Poison::default()),
                Box::new(Recharge::default()),
            ];

            // pick a spell
            for mut spell in possible_spells {
                let mut player_ = player.clone();
                let mut enemy_ = enemy.clone();
                let mut next_active_spells_ = next_active_spells.clone();

                spell.init(&mut player_, &mut enemy_);

                if player_.mana < 0 {
                    continue
                }

                // check if spell is already active
                if next_active_spells.iter().any(|spell_| { return spell.name() == spell_.name() }) {
                    continue
                }


                if !spell.has_timed_out() {
                    next_active_spells_.push(spell.clone());
                }

                let mut choices_ = choices.clone();
                choices_.push(spell.name());

                s.push_back(GameState{ player: player_, enemy: enemy_, active_spells: next_active_spells_.clone(), turn: turn + 1, used_mana: used_mana + spell.cost(), choices: choices_ })

            }

        } else {
            player.health -= max(enemy.damage - player.armour, 1);

            let choices_ = choices.clone();

            s.push_back(GameState{ player: player.clone(), enemy: enemy.clone(), active_spells: next_active_spells.clone(), turn: turn + 1, used_mana, choices: choices_ })
        }
    }
}

fn part2() {

    let content: String = fs::read_to_string("in").expect("Should be able to read from file");
    let lines: Vec<_> = content.split("\n").collect();

    let mut s: LinkedList<GameState> = LinkedList::new();
    s.push_back(GameState{
        player: Player { health: 50, armour: 0, mana: 500 },
        enemy: Enemy {
            health: i32::from_str(lines[0].split(" ").last().expect("There should be at least one token")).expect("Token should be an int"),
            damage: i32::from_str(lines[1].split(" ").last().expect("There should be at least one token")).expect("Token should be an int")
        },
        choices: vec![],
        active_spells: vec![], turn: 0, used_mana: 0});

    let mut min_mana: i32 = i32::MAX;

    while !s.is_empty() {
        let state = s.pop_front().unwrap();

        let mut player = state.player.clone();
        let mut enemy = state.enemy.clone();
        let active_spells = state.active_spells.clone();
        let used_mana = state.used_mana.clone();
        let turn = state.turn.clone();
        let choices = state.choices.clone();

        let mut next_active_spells: Vec<Box<dyn Spell>> = Vec::new();

        if used_mana > min_mana {
            continue;
        }

        // update all spells
        for mut spell in active_spells {
            spell.update(&mut player, &mut enemy);
            if !spell.has_timed_out() {
                next_active_spells.push(spell.clone());
            } else {
                spell.destroy(&mut player, &mut enemy);
            }
        }

        if player.health <= 0 {
            continue;
        } else if enemy.health <= 0 {
            if min_mana > used_mana {
                min_mana = used_mana;
                println!("Win at state: {:?}", state);
                println!("Min mana used {}", used_mana);
            }
        }


        if turn % 2 == 0 {
            // added for part 2
            player.health -= 1;
            if player.health <= 0 {
                continue
            }

            let possible_spells: Vec<Box<dyn Spell>> = vec![
                Box::new(MagicMissile),
                Box::new(Drain),
                Box::new(Shield::default()),
                Box::new(Poison::default()),
                Box::new(Recharge::default()),
            ];

            // pick a spell
            for mut spell in possible_spells {
                let mut player_ = player.clone();
                let mut enemy_ = enemy.clone();
                let mut next_active_spells_ = next_active_spells.clone();

                spell.init(&mut player_, &mut enemy_);

                if player_.mana < 0 {
                    continue
                }

                // check if spell is already active
                if next_active_spells.iter().any(|spell_| { return spell.name() == spell_.name() }) {
                    continue
                }


                if !spell.has_timed_out() {
                    next_active_spells_.push(spell.clone());
                }

                let mut choices_ = choices.clone();
                choices_.push(spell.name());

                s.push_back(GameState{ player: player_, enemy: enemy_, active_spells: next_active_spells_.clone(), turn: turn + 1, used_mana: used_mana + spell.cost(), choices: choices_ })

            }

        } else {
            player.health -= max(enemy.damage - player.armour, 1);

            let choices_ = choices.clone();

            s.push_back(GameState{ player: player.clone(), enemy: enemy.clone(), active_spells: next_active_spells.clone(), turn: turn + 1, used_mana, choices: choices_ })
        }
    }
}


fn main() {
    println!("###### Part 1 ######");
    part1();
    println!("###### Part 2 ######");
    part2();
}
