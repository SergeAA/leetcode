defmodule Solution do
  @spec roman_to_int(s :: String.t) :: integer

  def roman_to_int(s) do
    rtoi = fn r ->
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

    calc = fn
      x, {acc, prev} when x < prev -> {acc - x, x}
      x, {acc, _prev} -> {acc + x, x}
    end

    to_charlist(s)
      |> Enum.map(rtoi)
      |> Enum.reverse()
      |> Enum.reduce({0, 0}, calc)
      |> elem(0)
  end
end

IO.inspect(Solution.roman_to_int("XCIV"))
IO.inspect(Solution.roman_to_int("III"))
