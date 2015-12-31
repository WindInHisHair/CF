s = gets.strip.split
n = s[0].to_i
if s[-1] == 'week'
	w = {5 => 1, 6 => 2, 7 => 3, 1 =>4, 2 =>5, 3 =>6, 4 => 7}
	puts (366 -w[n])/7 +1

else 
	m = [31, 29, 31, 30, 31, 30,31,31,30, 31, 30, 31]
	res = 0
	m.each do |e|
		res += 1 if n <= e
	end
	puts res
end
