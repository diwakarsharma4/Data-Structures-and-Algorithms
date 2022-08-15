Given graph :

![prims-algorithm2](https://user-images.githubusercontent.com/101266746/184697639-afa743e6-f6c6-4716-9e01-2f2b83d418c8.png)<br><br>

Intially :<br>
distance = [inf, inf, inf, inf, inf]<br>
mstset =   [False, False, False, False, False]<br>
parent =   [None ,None ,None ,None , None]<br><br>

Preprocessing :<br>
distance = [0, inf, inf, inf, inf]<br>
mstset =   [False, False, False, False, False]<br>
parent =   [-1 ,None ,None ,None , None]<br>

![prims-algorithm2](https://user-images.githubusercontent.com/101266746/184697975-3c14a33e-1682-442e-b632-7ff350a07a7b.png)<br><br>


First go:<br>
distance = [0, inf, 3, inf, inf]<br>
mstset =   [True, False, False, False, False]<br>
parent =   [None ,None ,0 ,None , None]<br>

![prims-algorithm3](https://user-images.githubusercontent.com/101266746/184698017-4183319f-eef4-414f-a9bc-5f28185fccba.png)<br><br>


Second go:<br>
distance = [0, 10, 3, 2, 6]<br>
mstset =   [True, False, True, False, False]<br>
parent =   [None ,2 ,0 ,2 , 2]<br>

![prims-algorithm4](https://user-images.githubusercontent.com/101266746/184698130-1e788866-1b80-47c0-bc2f-af62e39821ee.png)<br><br>


Third go:<br>
distance = [0, 10, 3, 2, 6]<br>
mstset =   [True, True, True, False, False]<br>
parent =   [None ,2 ,0 ,2 , 2]<br>

![prims-algorithm5](https://user-images.githubusercontent.com/101266746/184698161-1016b1b0-628e-45bf-879c-517cf431bb00.png)<br><br>


Fourth go:<br>
distance = [0, 10, 3, 2, 1]<br>
mstset =   [True, True, True, True, False]<br>
parent =   [None ,2 ,0 ,2 , 3]<br>

![prims-algorithm6](https://user-images.githubusercontent.com/101266746/184698216-a9362961-34db-4ebe-af2c-c12553afd438.png)<br><br>


Fifth go:<br>
distance = [0, 10, 3, 2, 1]<br>
mstset =   [True, True, True, True, True]<br>
parent =   [None ,2 ,0 ,2 , 3]<br>

![prims-algorithm6](https://user-images.githubusercontent.com/101266746/184698216-a9362961-34db-4ebe-af2c-c12553afd438.png)
