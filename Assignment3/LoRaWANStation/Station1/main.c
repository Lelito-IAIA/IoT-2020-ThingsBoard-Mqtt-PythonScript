/*
 * Copyright (C) 2018 Inria
 *
 * This file is subject to the terms and conditions of the GNU Lesser
 * General Public License v2.1. See the file LICENSE in the top level
 * directory for more details.
 */

#include <string.h>

#include "xtimer.h"

#include "net/loramac.h"
#include "semtech_loramac.h"

#include "hts221.h"
#include "hts221_params.h"

#include "board.h"

/* Declare globally the loramac descriptor */
static semtech_loramac_t loramac;

/* Declare globally the sensor device descriptor */
static hts221_t hts221;


/* Device and application informations required for OTAA activation */
static const uint8_t deveui[LORAMAC_DEVEUI_LEN] = { 0x00, 0x27, 0x1A, 0x6D, 0x44, 0x82, 0x8D, 0x72 };
static const uint8_t appeui[LORAMAC_APPEUI_LEN] = { 0x70, 0xB3, 0xD5, 0x7E, 0xD0, 0x02, 0xD4, 0x49 };
static const uint8_t appkey[LORAMAC_APPKEY_LEN] = { 0x83, 0x5F, 0xD0, 0x1D, 0x19, 0x77, 0x81, 0xB0, 0xA0, 0xE3, 0x20, 0x9F, 0x02, 0xCA, 0x1A, 0xD0 };

//Generating Random Values
int get_random(int min, int max) { 
    int randValue = (rand() % (max - min + 1)) + min;
    return randValue;
}

//Generating the payload with random values
void get_payload(char* payload){
    int temp = get_random(-50,50);
    int hum = get_random(0,100);
    int win_dir = get_random(0,360);
    int win_int = get_random(0,100);
    int rain = get_random(0,50);

    sprintf(payload,"{\"Temperature\":\"%d Celsius\",\"Humidity\":\"%d %%\",\"Wind direction\":\"%d degrees\",\"Wind intensity\":\"%d m/s\",\"Rain height\":\"%d mm/h\"}",temp,hum,win_dir,win_int,rain);

}

static void sender(void)
{
    while (1) {
        //char message[32];
        /* sleep 20 secs */
        xtimer_sleep(20);

        /* do some measurements */
        //uint16_t humidity = 0;
        //int16_t temperature = 0;
        char payload[400];
        get_payload(payload);
        /*if (hts221_read_humidity(&hts221, &humidity) != HTS221_OK) {
            puts(" -- failed to read humidity!");
        }
        if (hts221_read_temperature(&hts221, &temperature) != HTS221_OK) {
            puts(" -- failed to read temperature!");
        }
            
        sprintf(message, "H: %u.%u, T:%u.%u",
                (humidity / 10), (humidity % 10),
                (temperature / 10), (temperature % 10));
        */
        printf("Sending data: %s\n", payload);

        /* send the LoRaWAN message */
        uint8_t ret = semtech_loramac_send(&loramac, (uint8_t *)payload,
                                           strlen(payload));
        if (ret != SEMTECH_LORAMAC_TX_DONE) {
            printf("Cannot send payload '%s', ret code: %d\n", payload, ret);
        }
    }

    /* this should never be reached */
    return;
}

int main(void)
{
    if (hts221_init(&hts221, &hts221_params[0]) != HTS221_OK) {
        puts("Sensor initialization failed");
        LED3_TOGGLE;
        return 1;
    }
    if (hts221_power_on(&hts221) != HTS221_OK) {
        puts("Sensor initialization power on failed");
        LED3_TOGGLE;
        return 1;
    }
    if (hts221_set_rate(&hts221, hts221.p.rate) != HTS221_OK) {
        puts("Sensor continuous mode setup failed");
        LED3_TOGGLE;
        return 1;
    }

    /* initialize the loramac stack */
    semtech_loramac_init(&loramac);

    /* use a fast datarate so we don't use the physical layer too much */
    semtech_loramac_set_dr(&loramac, 5);

    /* set the LoRaWAN keys */
    semtech_loramac_set_deveui(&loramac, deveui);
    semtech_loramac_set_appeui(&loramac, appeui);
    semtech_loramac_set_appkey(&loramac, appkey);

    /* start the OTAA join procedure */
    puts("Starting join procedure");
    if (semtech_loramac_join(&loramac, LORAMAC_JOIN_OTAA) != SEMTECH_LORAMAC_JOIN_SUCCEEDED) {
        puts("Join procedure failed");
        return 1;
    }

    puts("Join procedure succeeded");

    /* call the sender */
    sender();

    return 0; /* should never be reached */
}

