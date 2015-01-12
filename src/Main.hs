import Numeric.LinearAlgebra

disp = putStr . dispf 2
latex m = putStrLn $ latexFormat "array" (dispf 2 m)
m = (3><4)[1..] :: Matrix Double
--(q,r) = qr m

prim = [[[[i,j,k]| i<- [-3..3],j<- [-3..3],k<- [-3..3]],[[i,j,k]|i<- [-3..3],j<- [-3..3],k<- [-3..3]],[[i,j,k]|i<- [-3..3],j<- [-3..3],k<- [-3..3]]]]

main = do
  disp m
  latex m
