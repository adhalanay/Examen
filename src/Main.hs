import Numeric.LinearAlgebra
import Control.Monad

disp = putStr . dispf 2
latex m = putStrLn $ latexFormat "array" (dispf 2 m)

generator :: Int -> Int -> Int -> [Matrix Double]

generator s m n =
   xs = replicateM m [-s..s]
   

main = do
  disp m
  latex m
