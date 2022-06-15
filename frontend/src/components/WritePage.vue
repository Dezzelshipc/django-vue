<template>
<div>
    <router-link to="/home">Home</router-link>
    <br>
    <button class="btn btn-primary" @click="start">Start</button>
    <button @click="stop">Stop</button>
    <button @click="wordNumber++">add</button>
    <div>
        <span v-for="word, index in text"
            v-bind:key="word"
            class="text"
        ><span
            :class="{ under : index == wordNumber }"
        >{{ word }}</span>&nbsp;
        </span>
    </div>
    
    <input type="text" v-model="inText" @keypress.space="next" @keypress="press($event)">
    <br>
    {{ formattedElapsedTime }} {{ elapsedTime }} {{ this.timer }}
    <br>
    {{ inText }}
    <br>
    Сходится: {{ isCorrect }}
    <br>
    Длины слова: {{ this.started ? this.text[this.wordNumber].length : 0 }} Длина напечатанного: {{ this.inText.length }}
    <br>
    Номер слова: {{ wordNumber }} Длина текста: {{ this.started ? this.text.length : 0 }}
    <br>
    Победа: {{ win }} Ошибки: {{ miss }}
    <br>
    Знаков в минуту: {{ (lettersCount * 60000 / elapsedTime).toFixed(2) }} Знаки: {{ lettersCount }}
    <Button></Button>
</div>
</template>

<script>
import Button from 'primevue/button'

export default {
    components: {
        Button,
    },
    inject: [
        ['assets']
    ],
    data() {
        return {
            inText: '',
            started: 0,
            wordNumber: 0,
            text: [],
            music: [],
            win: 0,
            miss: 0,
            lettersCount: 0,

            elapsedTime: -3000,
            timer: undefined,
            audios: [
                //Сюда new Audio('url'),
            ],
        }
    },
    methods: {
        start() {
            this.inText = ''
            this.elapsedTime = -3000
            this.wordNumber = 0
            let text = "Сосны обступали тропу плотно, и, хотя истыканное их верхушками небо светилось голубым, в лесу было сумрачно. По тропинке вперёд бежали муравьи, большие, красные, по своим каким-то муравьиным делам."
            let music = "Db D Db D Bb G * * Bb G * * D G * * Db D Db D Bb G * * Bb G * * D G * * Db D Db D Bb G * * Bb G * * D G * * A Bb A Bb G D * * Db D G Bb Db * * * Db D Db D Bb G * * Bb G * * D G * * A Bb A Bb G D * * Db D G Bb Db * * * Db D Db D Bb G * * Bb G * * D G * * Db D Db D Bb G * * Bb G * * D G * *"
            this.lettersCount = 0
            this.text = text.split(' ')
            this.music = music.split(' ')
            this.started = 1;

            (new Audio(`https://assets.mixkit.co/sfx/preview/mixkit-simple-countdown-922.mp3`)).play()
            
            if (!this.timer) {
                this.timer = setInterval(() => {
                    this.elapsedTime += 10
                }, 10)
            }
        },
        next(event) {
            if (this.isCorrect && this.text[this.wordNumber].length === this.inText.length) {
                event.preventDefault()
                this.inText = ''
                if (this.wordNumber === this.text.length - 1) {
                    this.win = 1
                    this.stop()
                    return
                }
                this.wordNumber++
            }
        },
        stop() {
            clearInterval(this.timer)
            this.timer = undefined
        },
        reset() {
            this.elapsedTime = 0;
        },
        press(event) {
            if (this.elapsedTime < 0 || this.timer === undefined) {
                event.preventDefault()
            } else {
                this.lettersCount++
                
                if (this.isCorrect) {
                    let currentNote = this.lettersCount % this.music.length
                    if (this.music[currentNote] !== '*') {
                        let audio = new Audio(`http://localhost:8000/api/notes/1/notes_${this.music[currentNote]}.mp3`)
                        console.log(audio, this.music[this.lettersCount])
                        audio.play()
                    }
                }
            }
        },
    },
    computed: {
        isCorrect() {
            return this.started ? this.text[this.wordNumber].startsWith(this.inText.trim()) : 0
        },
        formattedElapsedTime() {
            const date = new Date(null);
            date.setMilliseconds(Math.abs(this.elapsedTime));
            const utc = date.toISOString()
            return (this.elapsedTime < 0 ? "-" : '' )+ utc.substr(utc.indexOf(":")+1, 8);
        }
    },
    watch: {
        isCorrect() {
            if (!this.isCorrect) {
                this.miss++
            }
        }
    }
}
</script>

<style>
.text {
    display: inline-block;
}
.under {
    text-decoration: underline;
}
</style>