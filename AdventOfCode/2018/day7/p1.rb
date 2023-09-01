
before = {}
after = {}

f = File.new("input", "r") # reading

f.readlines.map { |l| l.rstrip.split }.each { |line|
  fst = line[1]
  snd = line[-3]

  unless before.key?(fst)
    before[fst] = 0
  end
  unless before.key?(snd)
    before[snd] = 0
  end
  unless after.key?(fst)
    after[fst] = []
  end
  unless after.key?(snd)
    after[snd] = []
  end

  before[snd] += 1
  after[fst] << snd
}

puts before
puts after


remaining = before.keys.select { |e| before[e] == 0 }.sort
p remaining

order = ""
until remaining.empty?
  item = remaining.shift
  order << item
  p item
  after[item].each { |neigh|
    before[neigh] -= 1
    if before[neigh] == 0
      remaining.push(neigh)
      remaining.sort
    end
  }
end

p order






