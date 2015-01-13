import Numeric.LinearAlgebra

disp = putStr . dispf 2
latex m = putStrLn $ latexFormat "array" (dispf 2 m)
m = (3><4)[1..] :: Matrix Double
--(q,r) = qr m

generator :: [Matrix Double]

generator =
   lista=[[i

main = do
  disp m
  latex m
