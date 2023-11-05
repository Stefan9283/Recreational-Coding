

f = File.open("input", "r")

f.readline
f.readline

grid_ = []
max_x_ = 0
max_y_ = 0
f.readlines.each do |line|
  path, size, used, _, _ = line.split
  size = size.chars[0..-2].join('').to_i
  used = used.chars[0..-2].join('').to_i
  _, x, y = path.split("/")[-1].split("-")
  x = x.chars[1..-1].join('').to_i
  y = y.chars[1..-1].join('').to_i
  # puts "#{x}, #{y} ( #{used} / #{size} )"

  max_x_ = [max_x_, x].max
  max_y_ = [max_y_, y].max

  while x >= grid_.size
    grid_.push([])
  end

  while y > grid_[x].size
    grid_[x].push(nil)
  end

  grid_[x][y] = [used, size]

end


class Grid
  attr_accessor :grid, :max_x, :max_y
  def initialize
    @max_x = 0
    @max_y = 0
    @grid = []
  end

  def is_inside?(x, y)
    if x < 0 or x > @max_x or y < 0 or y > @max_y
      return false
    end
    true
  end
end

grid = Grid.new

grid.grid =grid_
grid.max_x = max_x_
grid.max_y = max_y_

p grid


