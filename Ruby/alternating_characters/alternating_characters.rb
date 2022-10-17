def alternating_characters?(string)
  type = [/[aeiou]/, /[^aeiou]/].cycle

  if string.start_with?(/[^aeiou]/)
    type.next
  end

  string.chars.all? { |ch| ch.match?(type.next) }
end

ans = alternating_characters?("ateciyu")
p ans
# true