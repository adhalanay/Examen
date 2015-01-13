import Numeric.LinearAlgebra
import Control.Monad

disp = putStr . dispf 2
latex m = putStrLn $ latexFormat "array" (dispf 2 m)

generator :: Int -> Int -> Int -> [[[Double]]]

generator s m 0 = []
generator s m n =
   let xs = replicateM m [-s..s]
       ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
   in  generator s m (n-1) ++ [ys]

main = do
  print $ generator 1 3 2
