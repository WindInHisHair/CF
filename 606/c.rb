#Good luk for the Contest 606, Problem: c
n = gets.strip.to_i
ar = gets.strip.split.map(&:to_i)

pos = Array.new(n, 0)
0.upto(n-1).each do |i|
	pos[ar[i]-1]  = i
end

res = 1
tmp = 1
1.upto(n-1).each do |i|
	if pos[i] > pos[i-1]
		tmp += 1
	else
		res = tmp if tmp >res
		tmp = 1
	end
end
res = tmp if tmp > res
puts n-res