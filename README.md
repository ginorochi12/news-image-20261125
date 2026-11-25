# The World Today — Wednesday, 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/ginorochi12/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/ginorochi12/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for make.fun's **news-image-20261125** bounty: sum up the world's news of
Wednesday 25 November 2026 in one image, $100 in USDC shared by the top 50.

## The image

![The World Today — 25 November 2026](entry.png)

A newspaper front page drawn with PIL for crisp, legible text:

- **Lead:** Zelenskiy confirms Ukraine hit a Russian ship in the Gulf of
  Finland and sank a warship off Libya; Norway urges caution.
- **Middle East:** Houthi drone strike hits Riyadh's tallest tower, 11 wounded.
- **USA / China:** Huawei convicted in a US criminal trial over its Iran business.
- **USA:** CIA and ODNI suffer a cybersecurity breach of unclassified information.
- **Europe:** NATO sends early-warning aircraft to Poland after missiles land there.
- **France:** Sarkozy and Carla Bruni's corruption case goes to trial.
- **Markets:** Nvidia slides 7% as lawmakers question Trump stock trades.
- **Also:** Trump awards Giuliani the Medal of Freedom; England beat Australia
  in the second T20I.

## The program

`main.py` (Python 3.13, standard library only) validates that `entry.png` is
a real PNG and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`, so both runs
of the program write identical bytes. No network is used.

## Sources

Headlines researched on 25 November 2026 from the Reuters world news summary
and same-day reporting (RFE/RL, Jagran Josh, Disclosure News).
