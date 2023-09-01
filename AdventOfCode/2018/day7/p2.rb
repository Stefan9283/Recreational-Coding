
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


WORKERS = 5
jobs_rem_time = []
(0...WORKERS).each do
  |_| jobs_rem_time.push([0, nil])
end

remaining = before.keys.select { |e| before[e] == 0 }.sort
# p remaining

time = 0
# TODO
until remaining.empty?

  (0...WORKERS).each { |i|
    seconds, node = jobs_rem_time[i]
    seconds -= 1
    if seconds <= 0
      jobs_rem_time[i] = [0, nil]
      if remaining.include?(node)
        remaining.delete(node)

        item = node
        after[item].each { |neigh|
          before[neigh] -= 1
          if before[neigh] == 0
            remaining.push(neigh)
            remaining.sort
          end
        }

      end
    else
      jobs_rem_time[i] = [seconds, node]
    end
  }


  (0...[WORKERS, remaining.size].min).each { |i|
    letter = remaining[i]
    # check if job in progress
    # if in progress then remove a second and if necessary update next nodes
    # if not then check if it can be assigned to a worker

    in_progress = false
    available_worker = -1

    j = 0
    jobs_rem_time.each { |job|
      _, job_letter = job
      if job_letter == letter
        in_progress = true
        break
      end

      if job_letter == nil
        available_worker = j
      end

      j += 1
    }

    # puts "#{letter} #{available_worker} #{in_progress}"

    unless in_progress
      if available_worker != -1
        jobs_rem_time[available_worker] = [letter.chars.first.ord - "A".chars.first.ord + 1 + 60, letter]
      end
    end

  }


  time += 1

  if time > 920
    break
  end
end

puts time - 1