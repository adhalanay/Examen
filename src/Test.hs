import Numeric.LinearAlgebra
import Control.Monad
--import Control.Monad.Random
--import System.Random.Mersenne.Pure64 (newPureMT)
--import RandomList
--import System.Random
import System.Random.Shuffle

generator :: Int -> Int -> Int -> [[[Double]]]
selection :: Int->Int->[[[Double]]] -> [[[Double]]]

generator s m 1 =
            let  xs = replicateM m [-s..s]
                 ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
            in [ys]
generator s m 2 =
           let xs = replicateM m [-s..s]
               ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
           in [[x]++[y] | x<- ys,y<- ys]
generator s m n =
      let xs = replicateM m [-s..s]
          ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
          zs = generator s m (n-1)
      in [x++[y]| x<- zs,y<- ys]


lrank = rank.fromLists

selection r1 r2 = filter (\a -> lrank  a >= r1 && lrank a <=r2)

main = do
          let xs = generator 2 5 4
              ys = take 1000 $ selection 2 2 xs
          zs <- shuffleM ys
          print $ take 50 zs
