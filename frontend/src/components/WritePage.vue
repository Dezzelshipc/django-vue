<template>
<div>
    <router-link to="/home">Home</router-link>
    <br>
    <div>
        <input type="radio" value=1 v-model="mode">
        <label>Text + Music</label>
        <br>
        <input type="radio" value=2 v-model="mode">
        <label>Random top 1000 russian words</label>
        <br>
        {{ mode }}
    </div>
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



import axios from 'axios'
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
            mode: 1,
        }
    },
    methods: {
        async start() {
            try {
                this.inText = ''
                this.elapsedTime = -3000
                this.wordNumber = 0

                this.lettersCount = 0
                if (this.mode == 1) {
                    const response = await axios.get('/api/assets/json/music.json')
                    const data = response.data

                    this.text = data[0].text.split(' ')
                    this.music = data[0].music.split(' ')
                } else if (this.mode == 2) {
                    const response = await axios.get('/api/assets/json/words.json')
                    const data = response.data
                    
                    this.text = data.sort(() => 0.5 - Math.random()).slice(0, 30 + Math.floor( Math.random() * 5))
                }
                this.started = 1;

                (new Audio(`/api/assets/audio/count_down.mp3`)).play()
                
                if (!this.timer) {
                    this.timer = setInterval(() => {
                        this.elapsedTime += 10
                    }, 10)
                }
            } catch {
                this.text = ['Server', 'error']
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
                
                if (this.isCorrect && this.music.length && this.mode === 1) {
                    let currentNote = this.lettersCount % this.music.length
                    if (this.music[currentNote] !== '*') {
                        let audio = new Audio(`/api/assets/audio/notes_${this.music[currentNote]}.mp3`)
                        audio.play()
                    }
                }
            }
        },
    },
    computed: {
        isCorrect() {
            return this.started && this.text.length ? this.text[this.wordNumber].startsWith(this.inText.trim()) : 0
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