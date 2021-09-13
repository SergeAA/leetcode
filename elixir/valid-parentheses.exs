defmodule Solution do
  @spec is_valid(s :: String.t) :: boolean
  def is_valid(s) do

    buffer = fn
      x, [] -> [x]
      ?), [?( | t] -> t
      ?], [?[ | t] -> t
      ?}, [?{ | t] -> t
      x, acc -> [x | acc]
    end

    case Enum.reduce(to_charlist(s), [], buffer) do
      [] -> true
      _  -> false
    end
  end
end

IO.inspect(Solution.is_valid("()()()([)"))
IO.inspect(Solution.is_valid("[({}([]))]"))
