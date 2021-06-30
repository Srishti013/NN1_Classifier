# NN1_Classifier for Time Series Analysis

* Results obtained by my model.

| ID  |  Name |  Train | Test | Class | Default Rate | Ed(w=0) |
|-----|-------|--------|------|-------|--------------|---------|
| 1	| Adiac	| 390 |	391 |	37	| 0.9642 |	0.9565	|
| 2 |	ArrowHead	| 36 |	175 |	3 | 0.6057 | 0.1143 |
| 3   | Beef  | 30     |  30 |   5    |   0.6333   |  0.2667 |
| 4   | BettleFly  | 20   |  20 |   2  |   0.5000   |  0.5000 |
| 5   | BirdChicken | 20   |  20 |   2  |   0.5000   |  0.0500 |
| 6   | Car | 60   |  60 |   4  |   0.7000 |  0.7333 |
| 7 |	CBF |	30 | 900 | 3 |	0.6644 | 0.6578	|	
| 8	|	ChlorineConcentration |	467	| 3840 |	3	|	0.7391 | 0.7391	|
| 10 | Coffee	| 28	| 28	| 2	|  	0.0714 | 0.0000 |
| 11 | Computers |	250	| 250	| 2 | 0.1480 | 0.2760 |
| 12 |	CricketX	| 390	| 390	| 12 | 0.9026 | 0.9026 |
| 13 | CricketY	| 390	| 390 |	12 |	0.9077 | 0.9051	|	
| 14 | CricketZ |	390 |	390	| 12	|	0.8923 | 0.8821	|
| 15	|	DiatomSizeReduction |	16	| 306	| 4	| 0.71240 | 0.7026	|
| 16	| DistalPhalanxOutlineAgeGroup |	400	| 139	| 3	|	 0.3022 | 0.3309 |
| 17	|	DistalPhalanxOutlineCorrect |	600	| 276	| 2 | 0.4239 | 0.4167	|
| 18	| DistalPhalanxTW	| 400	 |139	| 6 | 0.6835 |	0.6978	|
| 19	|	Earthquakes |	322 |	139 |	2	| 0.2518 | 0.2518 |
| 20	|	ECG200	| 100	| 100	| 2	| 0.3500 |	0.3600 |
| 21	|	ECG5000	| 500	| 4500 |	5	| 0.3333 |	0.3333 |
| 22 |	ECGFiveDays |	23 |	861	| 2	| 0.4983 | 0.4936 |	
| 23 |	ElectricDevices	| 8926 |	7711 |	7	| 0.7463	| 0.4492 |		
|24 |FaceAll	| 560	| 1690 | 14 | 0.9000 | 0.9000 |	
| 25	| FaceFour |	24 |	88 |	4	|	0.7273 | 0.6932	|
| 26	| FacesUCR | 200	| 2050	| 14	| 0.8546 | 0.9356 |
| 27	| FiftyWords	| 450	| 455	| 50 | 0.9033 | 0.9033 |
| 28	|	Fish	| 175	| 175	| 7	| 0.7886 |  0.8457	|	
| 29	| FordA	| 3601	| 1320	| 2	| 0.4841 | 0.3348 | 	
| 30	| FordB	| 3636	| 810	| 2	| 0.4951 | 0.3938	|
| 31	| GunPoint	| 50	| 150	| 2	| 0.4933 | 0.4933 |
| 32	|	Ham	| 109	| 105	| 2	| 0.5333 | 0.5619	|
| 33	| HandOutlines	| 1000	| 370	| 2	| 0.3595 | 0.1378 |
| 34 | Haptics	| 155	| 308	| 5	| 0.7890 | 0.7922 | 
| 35	| Herring	| 64	| 64	| 2	| 0.4844 | 0.4844 | 
| 36	| InlineSkate	| 100	| 550	| 7 | 0.8164 | 0.6582 |
| 37	| InsectWingbeatSound	| 220	| 1980	| 11 | 0.9091 | 0.4384 |





* Actual results

| ID  |  Name |  Train | Test | Class | Default Rate | Ed(w=0) |
|-----|-------|--------|------|-------|--------------|---------|
| 1	| Adiac	| 390 |	391 |	37	| 0.9591 |	0.3887	| 
| 2 |	ArrowHead	| 36 |	175 |	3 | 0.6057 | 0.2000|
| 3   | Beef  | 30     |  30 |   5    |   0.8000  |  0.3333 |
| 4   | BettleFly  | 20   |  20 |   2  |   0.5000   |  0.2500	 |
| 5   | BirdChicken | 20   |  20 |   2  |   0.5000   |  0.4500 |
| 6   | Car | 60   |  60 |   4  |   0.6833 |  0.2667 |
| 7 |	CBF |	30 | 900 | 3 |	0.6644 | 0.1478	|	
| 8	|	ChlorineConcentration |	467	| 3840 |	3	|	0.4674 | 0.3500	|
| 10 | Coffee	| 28	| 28	| 2	|  	0.4643 | 0.0000 |
| 11 | Computers |	250	| 250	| 2 | 0.5000 | 0.4240 |
| 12 |	CricketX	| 390	| 390	| 12 | 0.8974 | 0.4231 |
| 13 | CricketY	| 390	| 390 |	12 |	0.9051 | 0.4333	|	
| 14 | CricketZ |	390 |	390	| 12	|	0.8974 | 0.4128	|
| 15	|	DiatomSizeReduction |	16	| 306	| 4	| 0.6928 | 0.0654	|
| 16	| DistalPhalanxOutlineAgeGroup |	400	| 139	| 3	|	 0.5324 | 0.3741 |
| 17	|	DistalPhalanxOutlineCorrect |	600	| 276	| 2 | 0.4167 |0.2826	|
| 18	| DistalPhalanxTW	| 400	 |139	| 6 | 0.6978 |	0.3669	|
| 19	|	Earthquakes |	322 |	139 |	2	| 0.2518 | 0.2878 |
| 20	|	ECG200	| 100	| 100	| 2	| 0.3600 |	0.1200 |
| 21	|	ECG5000	| 500	| 4500 |	5	| 0.4162 |	0.0751 |
| 22 |	ECGFiveDays |	23 |	861	| 2	| 0.4971 | 0.2033 |	
| 23 |	ElectricDevices	| 8926 |	7711 |	7	| 0.7463	| 0.4492 |		
| 24 | FaceAll	| 560	| 1690 | 14 | 0.8302 | 0.2864 |	
| 25	| FaceFour |	24 |	88 |	4	|	0.7045 | 0.2159	|
| 26	| FacesUCR | 200	| 2050	| 14	| 0.8566 | 0.2307 |
| 27	| FiftyWords	| 450	| 455	| 50 | 0.8747 | 0.3692 |
| 28	|	Fish	| 175	| 175	| 7	| 0.8343 |0.2171	|	
| 29	| FordA	| 3601	| 1320	| 2	| 0.4841 | 0.3348 | 	
| 30	| FordB	| 3636	| 810	| 2	| 0.4951 | 0.3938	|
| 31	| GunPoint	| 50	| 150	| 2	| 0.4933 | 0.0867 |
| 32	|	Ham	| 109	| 105	| 2	| 0.4857 | 0.4000	|
| 33	| HandOutlines	| 1000	| 370	| 2	| 0.3595 | 0.1378 |
| 34 | Haptics	| 155	| 308	| 5	| 0.7825 | 0.6299 | 
| 35	| Herring	| 64	| 64	| 2	| 0.4063 | 0.4688 | 
| 36	| InlineSkate	| 100	| 550	| 7 | 0.8164 | 0.6582 |
| 37	| InsectWingbeatSound	| 220	| 1980	| 11 | 0.9091 | 0.4384 |
