#what the f**k the problem statement was talking about.
#Good luk for the Contest 606, Problem: b

X, Y, x, y = gets.strip.split.map(&:to_i)
cmd = gets.strip.split('')

mp = Array.new(X){Array.new(Y,1)}

pos = [x-1, y-1]
res = Array.new
cmd.each do |c|

	res << mp[pos[0]][pos[1]]
	mp[pos[0]][pos[1]] = 0
	next if pos[0] == 0 and c == 'U'
	next if pos[0] == X-1 and c == 'D'
	next if pos[1] == 0 and c == 'L'
	next if pos[1] == Y-1 and c == 'R'
	case c
	when 'U'
		pos[0] -=1
	when 'D'
		pos[0] += 1
	when 'L'
		pos[1] -= 1
	when 'R'
		pos[1] += 1
	end

  end

res << mp.reduce(0){|r,v| r += v.reduce(:+)}

res.each do |e|
	print e,' '
end
print "\n"
