#include "words.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** read_words(size_t *num_words){ 
    char **array = (char **)malloc(sizeof(char *));
    //char *wort = (char *)malloc(sizeof(char));
    char wort[14];
    // wort[0]= '\0';
    size_t counterX = 0; 
    // size_t wortlaenge = 1;                         
    while(scanf("%13s", wort) != EOF){
        array = (char **)realloc(array, sizeof(char *) * (counterX + 1));
        array[counterX] = malloc(sizeof(char) * (strlen(wort)+1));
        if(array[counterX]){ 
            strcpy(array[counterX], wort);
        } 
        
        counterX++; 
    }
//     char x;
//     int habewort = 0; 
//     while(scanf("%c", &x) != EOF){
//         if(x != ' ' && x != '\n'){
            
//             wort = (char *)realloc(wort, sizeof(char) * (wortlaenge +1));
//             wort[wortlaenge - 1] = x; // -1 weil ein Array von 0 anfängt!
//             // wort[wortlaenge - 1] = x;
//             habewort = 1;
//             wortlaenge++;
            
//         } else if(habewort == 1) {
//             array = (char **)realloc(array, sizeof(char *) * (counterX +1));
//             array[counterX] = malloc(sizeof(char) * (wortlaenge + 1));
//             // if (wortlaenge > 14){
//  //     array[counterX] = realloc(array[counterX],sizeof(char) * (strlen("Fehler13") + 1));
//             //     strcpy(array[counterX], "Fehler13");
//             // } else{
//                 if(wort!= NULL){
//                     memcpy(array[counterX], wort, wortlaenge);
//                 } else{
//                     memcpy(array[counterX], "fehler", strlen("fehler"));
//                 }
                
//             // }
//             free(wort);
//             wort = malloc(sizeof(char*));
//             // memset(wort, 0, 14);
//             // wort[0] = '\0';
//             habewort = 0;
//             wortlaenge = 1;
//             counterX++;
//         }
//     }
    //free(wort);
     *num_words = counterX;
     return array;
}

void print_words(char **words, size_t num_words){
    for(size_t i = 0; i < num_words; i++){
        if(words[i] != NULL){
            printf("%ld %s\n", i + 1, words[i]);
        }
        
    }
}

void free_words(char **words, size_t num_words){
    for (size_t i = 0; i< num_words; i++){
        free(words[i]);
    }
    free(words);
}
