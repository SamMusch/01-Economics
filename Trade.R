library(tradestatistics)
library(DT)
library(tidyverse)
datatable(ots_tables)

import_size_2020 <- ots_create_tidy_data(
  years = 2020,
  reporters = c("usa"),
  #partners = "arg",
  table = "yrp"
) %>% 
  mutate(totals = sum(trade_value_usd_imp),
         pct_total = formatC(100 * trade_value_usd_imp / totals), digits=2) %>%
  select(partner_iso, trade_value_usd_imp, pct_total) %>%
  arrange(desc(trade_value_usd_imp)) 



data_first <- ots_create_tidy_data(
  years = 1962:2020,
  reporters = c("usa"),
  table = "yrp"
)

data <- data_first %>% 
  select(year, partner_iso, trade_value_usd_imp) %>%
  dplyr::mutate(trade_value_usd_imp = replace_na(trade_value_usd_imp, 0)) %>%
  drop_na() %>%
  group_by(year) %>%
  arrange(desc(trade_value_usd_imp)) %>%
  mutate(rank=row_number()) %>%
  filter(rank<=10) %>% 
  mutate(year = lubridate::ymd(year, truncated = 2L)) %>%
  as_tibble()

library(lubridate)
library(gganimate)
library(hrbrthemes)
# https://www.r-bloggers.com/2019/04/how-to-create-a-bar-chart-race-in-r-mapping-united-states-city-population-1790-2010/

p <- data %>%
  ggplot(aes(x = -rank, y = trade_value_usd_imp, group = partner_iso)) +
  geom_tile(aes(y = trade_value_usd_imp / 2, height = trade_value_usd_imp, fill = partner_iso), width = 0.9) +
  geom_text(aes(label = partner_iso), hjust = "right", colour = "black", fontface = "bold", nudge_y = -100000) +
  geom_text(aes(label = scales::comma(trade_value_usd_imp)), hjust = "left", nudge_y = 100000, colour = "grey30") +
  coord_flip(clip="off") +
  #scale_fill_manual(name = 'Region', values = c("#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3")) +
  scale_x_discrete("") +
  scale_y_continuous("",labels=scales::comma) +
  hrbrthemes::theme_ipsum(plot_title_size = 32, subtitle_size = 24, caption_size = 20, base_size = 20) +
  theme(panel.grid.major.y=element_blank(),
        panel.grid.minor.x=element_blank(),
        legend.position = c(0.4, 0.2),
        plot.margin = margin(1,1,1,2,"cm"),
        axis.text.y=element_blank()) +
  # gganimate code to transition by year:
  transition_time(year) +
  ease_aes('cubic-in-out') +
  labs(title='Largest Cities in the United States',
       subtitle='Population in {round(frame_time,0)}',
       caption='Source: United States Census
michaeltoth.me / @michael_toth')

animate(p, nframes = 750, fps = 25, end_pause = 50, width = 1200, height = 900)

data