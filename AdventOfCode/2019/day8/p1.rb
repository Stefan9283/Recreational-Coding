w = 25
h = 6

line = File.open('input', 'r').readline

step = 25 * 6

zeroes = line.size
ones = 0
twos = 0

(0...line.length).step(step).each do |i|
  layer = line.slice(i, step)

  zeroes_ = layer.count('0')

  if zeroes_ < zeroes
    zeroes = zeroes_
    ones = layer.count('1')
    twos = layer.size - ones - zeroes
  end
end

puts ones * twos
