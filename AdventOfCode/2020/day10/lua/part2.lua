local arr = { 0 }

local last = 0
for line in io.lines('input1') do
    arr[#arr + 1] = tonumber(line)
    last = math.max(last, arr[#arr])
end

local dp = {}
dp[last + 3] = 1

arr[#arr + 1] = last + 3
table.sort(arr, function(a, b) return a > b end)

for i, val in pairs(arr) do
    if i == 1 then
        goto continue
    end
    dp[val] = 0
    for j = 1, 3, 1 do
        if i - j > 0 and arr[i - j] - val <= 3 then
            dp[val] = dp[val] + dp[arr[i - j]]
        end
    end
    ::continue::
end

print(dp[arr[#arr]])

-- (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
-- (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
-- (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
-- (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
-- (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
-- (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
-- (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
-- (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
--
-- dp[0] = dp[1] = 8
-- dp[1] = dp[4] = 8
-- dp[4] = dp[5] + dp[6] + dp[7] = 8
-- dp[5] = dp[6] + dp[7] = 4
-- dp[6] = dp[7] = 2
-- dp[7] = dp[10] = 2
-- dp[10] = dp[11] + dp[12] = 2
-- dp[11] = dp[12] = 1
-- dp[12] = dp[15] = 1
-- dp[15] = dp[16] = 1
-- dp[16] = dp[19] = 1
-- dp[19] = dp[22] = 1
-- dp[22] = 1
-- result = dp[0] = 8
