
local arr = {}

for line in io.lines('input0') do
    arr[#arr + 1] = tonumber(line)
end
table.sort(arr)

local diff1 = 0
local diff3 = 1

local init0 = 0
for i = 1, #arr, 1 do
    local diff = arr[i] - init0
    init0 = arr[i]
    if diff == 3 then
        diff3 = diff3 + 1
    elseif diff == 1 then
        diff1 = diff1 + 1
    end
end

print(diff1 * diff3)
