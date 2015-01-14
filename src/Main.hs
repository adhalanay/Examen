import Numeric.LinearAlgebra
import Control.Monad

disp = putStr . dispf 2
latex m = putStrLn $ latexFormat "array" (dispf 2 m)

generator :: Int -> Int -> Int -> [[[Double]]]
conversion :: [[[Double]]] -> [Matrix Double]
selection :: Int->Int->[Matrix Double] -> [Matrix Double]

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
	    zs = generator s m (n-1)
	in [x++[y]| x<- zs,y<-ys]

conversion = map fromLists 

selection r1 r2 = filter (\a -> rank a >= r1 && rank a <=r2)

main = do
    let xs = generator 2 5 3
        ys = take 10 $ selection 1 2 (conversion xs)
        l = length ys
    print ys 