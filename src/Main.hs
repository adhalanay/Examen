import Numeric.LinearAlgebra
import Control.Monad
import Control.Monad.Random
--import System.Random.Mersenne.Pure64 (newPureMT)
--import RandomList

choose _ [] = error "choose: index out of range"
choose 0 (x:xs) = (x, xs)
choose i (x:xs) = let (y, ys) = choose (i - 1) xs in (y, x:ys)

shuffle :: Int -> Int -> [a] -> [a]
shuffle seed 0 _ = []
shuffle seed len xs =
    let
       n = fst $ randomR (0, len - 1) (mkStdGen seed)
       (y, ys) = choose n xs
       ys' = shuffle seed (len - 1) ys
    in y:ys'

disp = putStr . dispf 2
latex m = putStrLn $ latexFormat "array" (dispf 2 m)

generator :: Int -> Int -> Int -> [[[Double]]]
conversion :: [[[Double]]] -> [Matrix Double]
selection :: Int->Int->[Matrix Double] -> [Matrix Double]
disp_ls :: [Matrix Double] -> IO()

disp_ls [] = disp $ fromLists [[]]
disp_ls [x] = disp x
disp_ls (x:xs) = do
      disp x
      disp_ls xs

generator s m 1 =
           let xs = replicateM m [-s..s]
               ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
               zs = shuffle 18495758398490 (length ys) ys
           in [zs]
generator s m 2 =
           let xs = replicateM m [-s..s]
               ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
               ys1 = shuffle 10094748500790 (length ys) ys
               ys2 = shuffle 963547459682435 (length ys1) ys1
           in [[x]++[y] | x<- ys1,y<- ys2]
generator s m n =
      let xs = replicateM m [-s..s]
          ys = [[fromIntegral z :: Double | z <- x] | x <- xs]
          ys1 = shuffle 5302946104563828 (length ys) ys
          zs = generator s m (n-1)
          zs1 = shuffle 674857894620857 (length zs) zs
      in [x++[y]| x<- zs1,y<- ys1]

conversion = map fromLists

selection r1 r2 = filter (\a -> rank a >= r1 && rank a <=r2)

main = do
      let xs = generator 2 5 4
          ys = take 500 $ selection 2 2 (conversion xs)
          zs = shuffle 89309170391038948 (length ys) ys
          zss = take 10 zs
      disp_ls zss
