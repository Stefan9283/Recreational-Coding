w = 25
h = 6

line = File.open('input', 'r').readline

step = w * h

layer = '2' * step

(0...line.length).step(step).each do |i|
  layer_ = line.slice(i, step)
  (0...step).each do |j|
    if layer[j] == '2'
      layer[j] = layer_[j]
    end
  end
end

(0..step).step(w).each do |i|
  puts layer.slice(i, w).gsub!('0', ' ')
end
