# BIKE FINDER

I am officially tired for scanning MTB online stores for available bikes. Going the lazy route.

## Instructions

### Clone and Build

You'll need Git CLI, Docker or Podman on your system.

To build / run it as-is...

```bash
$ git clone {bike-finder-repo} bike-finder
$ cd bike-finder
$ ./run

```

### The results

The binary should build and execute the container and small Python (crap) code and return somethig like this.

```
STEP 1: FROM python:3.9-alpine
STEP 2: ARG PHANTOM_BINARY="phantomjs-2.1.1-linux-x86_64.tar.bz2"
--> Using cache 714b81d77cb9596f7a03c97137fdde26de06ca4aa06b2df75fe37f33c80e8676
--> 714b81d77cb
STEP 3: ARG GECKO_VERSION="v0.29.1"
--> Using cache 3c1e6c8f5554aab2c66a867074535fcd30082056fd8a5809391cf89964bdfb59
--> 3c1e6c8f555
STEP 4: ARG GECKO_PACKAGE="geckodriver-${GECKO_VERSION}-linux64.tar.gz"
--> Using cache 228e50f1c4a55de2318ac26176c22ed9e10c50da00d3505d495c9f98b4d55785
--> 228e50f1c4a
STEP 5: RUN apk update &&     apk add         curl         bzip2         tar         firefox-esr
--> Using cache dc94d03ca08b457af536c9fb231e6ff88db8e6f9e118824be7e3d390ef02c236
--> dc94d03ca08
STEP 6: RUN pip install     selenium     tabulate
--> Using cache fc1643376c80ea1da96d331dc9b5b858fdaa67ca9274a63e1601fac10c6ce197
--> fc1643376c8
STEP 7: RUN curl -sSL         https://bitbucket.org/ariya/phantomjs/downloads/${PHANTOM_BINARY}         -o ${PHANTOM_BINARY} &&     bzip2 --decompress ${PHANTOM_BINARY} &&     tar xvf ${PHANTOM_BINARY%.*} &&     mv ${PHANTOM_BINARY%.*.*}/bin/phantomjs /usr/bin/ &&     rm -rf ${PHANTOM_BINARY%.*.*} &&     rm ${PHANTOM_BINARY%.*}
--> Using cache cc7c3db3246bc63e9a4ddb28bb14845c3b85ee1528192e8344d914b95c319ee3
--> cc7c3db3246
STEP 8: RUN curl -sSL         https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/${GECKO_PACKAGE}         -o ${GECKO_PACKAGE} &&     tar zxvf ${GECKO_PACKAGE} &&     mv geckodriver /usr/bin/ &&     rm ${GECKO_PACKAGE}
--> Using cache 3340cf3f88e4b191a1ca5254e27fd7fffa5d18322eaaed96f7f883b52e8946d1
--> 3340cf3f88e
STEP 9: COPY ./src/main.py /main.py
--> Using cache b7926585ea9bd20d8720ef4c21dca35605341d484a62ecc219bc01daebca661e
--> b7926585ea9
STEP 10: ENTRYPOINT ["python", "main.py"]
--> Using cache 979c3d1ade8aa6b5011a66d3124b9799a08569effc070506c23fc1d454a1e082
STEP 11: COMMIT bike-finder:latest
--> 979c3d1ade8
979c3d1ade8aa6b5011a66d3124b9799a08569effc070506c23fc1d454a1e082

store      name                                                  price
---------  ----------------------------------------------------  -----------------------
CADENCE    CANNONDALE SCALPEL CARBON SE 1                        $6,100.00
BIKEMART   DIAMONDBACK CATCH 1 - 2021                            $2,550.00
BIKEMART   DIAMONDBACK RELEASE 29 3 - 2021                       $4,050.00
JENSONUSA  EMINENT ONSET LT ADVANCED BIKE 2021                   $6,199.00
JENSONUSA  EMINENT ONSET LT COMP BIKE 2021                       $4,699.00
JENSONUSA  EMINENT ONSET LT GX BIKE 2021                         $5,499.00
JENSONUSA  EMINENT ONSET MT COMP BIKE 2021                       $4,899.00
JENSONUSA  EMINENT ONSET ST COMP BIKE 2021                       $4,599.00
JENSONUSA  EMINENT ONSET X01 JENSON USA EXCLUSIVE BUILD          $5,800.00
CADENCE    GIANT REIGN ADVANCED PRO 29 1                         $5,750.00
CADENCE    GIANT STANCE 29 1                                     $2,100.00
BIKEMART   GIANT TRANCE ADVANCED PRO 29 0 - 2020                 $10,500.00
JENSONUSA  GT SENSOR CARBON PRO 29" BIKE 2020                    $5,500.00
JENSONUSA  IBIS RIPMO AF GX BIKE 2021                            $4,299.00
JENSONUSA  INTENSE PRIMER 29" ELITE BIKE 2020                    $6,999.00
JENSONUSA  NINER RIP 9 RDO 29 3-STAR BIKE 2021                   $5,400.00
JENSONUSA  NINER RIP 9 RDO 29 4-STAR BIKE 2021                   $6,300.00
JENSONUSA  NORCO TORRENT HT S1 29" 2021 BIKE                     $3,399.00
JENSONUSA  ORBEA RALLON M-LTD BIKE 2021                          $8,999.00
BIKEMART   ORBEA RISE M10 20MPH - 2021                           $8,599.00
BIKEMART   ORBEA RISE M20 20MPH - 2021                           $6,999.00
CADENCE    PIVOT CYCLES MACH 4 SL RACE X01                       $5,999.00
BIKEMART   SALSA SPEARFISH CARBON SLX - 2020                     $4,499.00 - $4,799.00
BIKEMART   SANTA CRUZ 5010 CC X01 RESERVE - 2021                 $8,949.00
BIKEMART   SANTA CRUZ HECKLER 1.0 CC XO1 RESERVE - 2020          $10,599.00
BIKEMART   SANTA CRUZ HECKLER CC R - 2021                        $7,699.00
BIKEMART   SANTA CRUZ HECKLER MX CC X01 RSV - 2021               $3,999.00 - $12,099.00
BIKEMART   SANTA CRUZ HECKLER MX CC XT - 2021                    $3,999.00 - $9,899.00
JENSONUSA  SANTA CRUZ HIGHTOWER 2 C XT-KIT BIKE 2021             $6,099.00
BIKEMART   SANTA CRUZ NOMAD 5 CC X01 RSV - 2021                  $9,599.00
CADENCE    SPECIALIZED EPIC EVO                                  $3,800.00
CADENCE    SPECIALIZED EPIC EXPERT                               $6,200.00
CADENCE    SPECIALIZED TURBO LEVO COMP                           $7,499.99 - $7,500.00
BIKEMART   SPECIALIZED TURBO LEVO SL COMP - 2021                 $7,000.00
BIKEMART   SPECIALIZED TURBO LEVO SL COMP CARBON - 2021          $8,000.00
CADENCE    SPECIALIZED TURBO MEN'S S-WORKS TURBO LEVO            $12,050.00
BIKEMART   SPECIALIZED TURBO TURBO LEVO SL EXPERT CARBON - 2021  $10,000.00
BIKEMART   TREK FUEL EX 9.9 X01 - 2021                           $7,499.99 - $7,999.99
BIKEMART   TREK SUPERCALIBER 9.9 XX1 AXS - 2021                  $10,499.99 - $10,999.99
```

The default returns a list of trail/all-mountain bikes, size large and in-store/stock.

## Customizing the search

- It should be relatively self-explanatory, so just start by looking under `./src/main.py`

## Final notes

- Open an issue if you have questions
- If you wan to make it better, please fork, tweak and open a pull request.