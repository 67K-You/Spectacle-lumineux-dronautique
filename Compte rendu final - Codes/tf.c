#include <stdint.h>
#include <stdlib.h>
#include "stm32fxxx.h"

#include "FreeRTOS.h"
#include "timers.h"

#include "deck.h"
#include "param.h"
.
 */
#define LED_ON HIGH
#define LED_OFF LOW

/* Define which IOs on the expansion deck is used */
#define BLUE_LED     DECK_GPIO_IO1

/* Enumeration for setting different states */
typedef enum {
    tf_off = 0,
    tf_on = 1
} TF;
static TF tf;

/* Timer loop and handle */
static xTimerHandle timer;
static void tfTimer(xTimerHandle timer)
{
  digitalWrite(BLUE_LED, LED_ON);
}

/* Main initialization */
static void tfInit(DeckInfo *info)
{
  pinMode(BLUE_LED, OUTPUT);

  digitalWrite(BLUE_LED, LED_ON);

  timer = xTimerCreate( "tfTimer", M2T(10),
                         pdTRUE, NULL, tfTimer );
  xTimerStart(timer, 100);
}

PARAM_GROUP_START(tf)
PARAM_ADD(PARAM_UINT32, state, &tf)
PARAM_GROUP_STOP(tf)

static const DeckDriver tf_deck = {
  .vid = 0,
  .pid = 0,
  .name = "bcTF",
  .usedGpio = DECK_USING_PB4 | DECK_USING_PB5 | DECK_USING_PB8,
  .init = tfInit,
};

DECK_DRIVER(tf_deck);
