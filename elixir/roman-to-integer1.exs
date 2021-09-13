defmodule Solution do
  @spec roman_to_int(s :: String.t) :: integer

  def rtoi(r) do
    case r do
      ?I -> 1
      ?V -> 5
      ?X -> 10
      ?L -> 50
      ?C -> 100
      ?D -> 500
      ?M -> 1000
      _ -> 0
    end
  end

  def cmc(h, {acc, prev}) do
    cur = Solution.rtoi(h)
    if prev > 0 and cur > prev do
      {acc + cur - 2*prev, cur}
    else
      {acc + cur, cur}
    end
  end

  def roman_to_int(s) do
    {res, _} = Enum.reduce(to_charlist(s), {0, 0}, &Solution.cmc/2)
    res
  end
end

IO.inspect(Solution.roman_to_int("XCIV"))
IO.inspect(Solution.roman_to_int("III"))
