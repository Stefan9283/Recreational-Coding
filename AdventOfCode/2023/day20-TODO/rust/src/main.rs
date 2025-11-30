use std::{collections::HashMap, fmt::Display, fs};

#[derive(Debug)]
enum ModuleType {
    Broadcaster,
    FlipFlop,
    Conjunction,
}

#[derive(Debug)]
struct Module {
    outputs: Vec<String>,
}

#[derive(Debug)]
struct Conjunction {
    module: Module,
    inputs: HashMap<String, bool>,
}

#[derive(Debug)]
struct FlipFlop {
    module: Module,
    state: bool,
}

#[derive(Debug)]
struct Broadcaster {
    module: Module,
}

#[derive(Debug)]
struct Event {
    module_name: String,
    signal: bool,
}

trait ModuleTrait: std::fmt::Debug {
    fn get_updated(&mut self, e: Event) -> Vec<Event>;
    fn update_outputs(&mut self) -> Vec<Event>;
    fn get_ouputs(&self) -> Vec<String>;
    fn add_input(&mut self, input: String);
}

impl ModuleTrait for FlipFlop {
    fn update_outputs(&mut self) -> Vec<Event> {
        let mut events = Vec::new();

        for output in &self.module.outputs {
            // create an event
            events.push(Event {
                module_name: output.clone(),
                signal: self.state,
            });
        }
        events
    }

    fn get_updated(&mut self, e: Event) -> Vec<Event> {
        if e.signal == false {
            self.state = !self.state;
        }
        return self.update_outputs();
    }

    fn get_ouputs(&self) -> Vec<String> {
        return self.module.outputs.clone();
    }

    fn add_input(&mut self, _input: String) {}
}

impl ModuleTrait for Conjunction {
    fn update_outputs(&mut self) -> Vec<Event> {
        let mut events = Vec::new();

        let mut signal = true;
        for input in self.inputs.values() {
            signal &= *input;
        }

        for output in &self.module.outputs {
            // create an event
            events.push(Event {
                module_name: output.clone(),
                signal,
            });
        }

        events
    }

    fn get_updated(&mut self, e: Event) -> Vec<Event> {
        self.inputs.insert(e.module_name, e.signal);
        return self.update_outputs();
    }

    fn get_ouputs(&self) -> Vec<String> {
        return self.module.outputs.clone();
    }

    fn add_input(&mut self, input: String) {
        self.inputs.insert(input, false);
    }
}

impl ModuleTrait for Broadcaster {
    fn update_outputs(&mut self) -> Vec<Event> {
        let mut events = Vec::new();

        for output in &self.module.outputs {
            // create an event
            events.push(Event {
                module_name: output.clone(),
                signal: false,
            });
        }

        events
    }

    fn get_updated(&mut self, _e: Event) -> Vec<Event> {
        return self.update_outputs();
    }

    fn get_ouputs(&self) -> Vec<String> {
        return self.module.outputs.clone();
    }

    fn add_input(&mut self, _input: String) {}
}

impl Module {
    fn new(outputs: Vec<String>) -> Self {
        Self { outputs }
    }
}


fn main() {
    let content = fs::read_to_string("in0").expect("Should be able to read the input from file");

    let mut modules: HashMap<String, Box<dyn ModuleTrait>> = HashMap::new();

    for line in content.lines() {
        let type_: ModuleType;

        let line = line.trim().replace(" ", "");

        let tokens: Vec<&str> = line.split("->").collect();
        let outputs: Vec<&str> = tokens[1].split(",").collect();

        let module_name = &tokens[0][1..tokens[0].len()];

        if line.chars().nth(0).unwrap() == '%' {
            type_ = ModuleType::FlipFlop;
        } else if line.chars().nth(0).unwrap() == '&' {
            type_ = ModuleType::Conjunction;
        } else {
            type_ = ModuleType::Broadcaster;
        }

        modules.insert(
            module_name.to_string(),
            match type_ {
                ModuleType::Broadcaster => Box::new(Broadcaster {
                    module: Module::new(outputs.iter().map(|s| s.to_string()).collect()),
                }),
                ModuleType::FlipFlop => Box::new(FlipFlop {
                    module: Module::new(outputs.iter().map(|s| s.to_string()).collect()),
                    state: false,
                }),
                ModuleType::Conjunction => Box::new(Conjunction {
                    module: Module::new(outputs.iter().map(|s| s.to_string()).collect()),
                    inputs: HashMap::new(),
                }),
            },
        );
    }


    for name in modules.keys().cloned().collect::<Vec<String>>() {
        let module = modules.get_mut(&name).unwrap();
        for output in module.get_ouputs() {
            let other_module = modules.get_mut(&output).unwrap();
            other_module.add_input(name.clone());
        }
    }


    println!("{:?}", modules);

}
