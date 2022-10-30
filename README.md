# CourseReco-engine

recommender engine for the Course Recommender project 

## Installation

just clone this repo

```bash
git clone https://github.com/HackerHub-ucdavis/CourseReco-engine
```

## Run

```bash
python start_engine.py
```

## CLI arguments

```bash
python start_engine.py -h
```

## Mode

this engine has two modes: full and sub

### Full

this mode fetches data from SchedGo server,
and make recommendations for all available courses for a quarter.

```bash
python start_engine.py --mode full
```

### Sub

This mode will only make recommendations with subjects Math, Statistics, and Computer Science.

**NOTE** this is the **default** mode.

```bash
python start_engine.py
# or
python start_engine.py -- mode ecs_mat_sta
```

# ToDo

* [x] compute similarity matrix only once when the engine starts
* [x] Integration with SchedGo
* [ ] error management (liked_key may not exists), and logs
* [ ] complete unit tests
* [ ] better recommendation methods
