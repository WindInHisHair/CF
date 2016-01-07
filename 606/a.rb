#Good luk for the Contest 606, Problem: a
have = gets.strip.split.map(&:to_i)
need = gets.strip.split.map(&:to_i)

res= 0
have.each_with_index do |v, i|
	if v > need[i]
		res += (v-need[i])/2
	elsif v < need[i]
		res -= need[i]-v
	end
end

puts res >= 0? 'Yes' : 'No'
