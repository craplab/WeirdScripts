def sum_eq_n?(arr, n)
  return true if arr.empty? && n == 0
  # arr.product
  # [[1], [2], [3], [4], [5]]

  # arr.product(arr)
  # [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], 
  # [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], 
  # [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], 
  # [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], 
  # [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]

  # arr.product(arr).reject { |a, b| a == b }
  # deletes the pairs where the first element is equal to the second element

  # And then we check using the .any? method if any of the pairs sum up to n

  arr.product(arr).reject { |a,b| a == b }.any? { |a,b| a + b == n }
end

puts sum_eq_n?([1,2,3,4,5], 9)
puts sum_eq_n?([1,2,3,4,5], 10)