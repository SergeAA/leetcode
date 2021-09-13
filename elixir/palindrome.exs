defmodule Solution do
  @spec is_palindrome(x :: integer) :: boolean
  def is_palindrome(x) do
    lst = to_charlist(to_string(x))

    case Enum.reverse(lst) do
      ^lst -> true
      _ -> false
    end

  end
end
