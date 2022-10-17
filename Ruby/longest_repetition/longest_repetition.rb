def longest_repetition(string)
  # string.chars
  # ["a", "a", "a", "b", "b"]
  
  # string.chars.chunk(&:itself)
  #<Enumerator: #<Enumerator::Generator:0x000000013a25e898>:each>

  # string.chars.chunk(&:itself).map(&:last)
  # [["a", "a", "a"], ["b", "b"]]

  # string.chars.chunk(&:itself).map(&:last).max_by(&:size)
  # ["a", "a", "a"]
  max = string
          .chars
          .chunk(&:itself)
          .map(&:last)
          .max_by(&:size)

  max ? [max[0], max.size] : ["", 0]
end

answer = longest_repetition("aaabb")
puts answer

# Example
# longest_repetition("aaaabb") # Outputs ["a",4]
