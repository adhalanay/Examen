import Numeric.LinearAlgebra
import Control.Monad

disp = putStr . dispf 2
latex m = putStrLn $ latexFormat "array" (dispf 2 m)

generator :: Int -> Int -> Int -> [[[Double]]]

generator s m 1 = 
	let xs = replicateM m [-s..s]
	    ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
    in  [ys]
generator s m 2 =
   let xs = replicateM m [-s..s]
       ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
    in  [[x]++[y] | x<-ys,y<-ys]
generator s m n =
	let xs = replicateM m [-s..s]
	    ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
	in [x++[y]| x<- generator s m (n-1),y<-ys]

main = do
	print $ generator 2 5 3 