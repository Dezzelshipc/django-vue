<template>
<div>
    <div>
        <div>
            <input class="form-check-input" type="radio" value=1 v-model="mode">
            <label class="form-check-label">Text + Music</label>
            <input class="form-check-input" type="radio" value=2 v-model="mode">
            <label class="form-check-label">Random top 1000 russian words</label>
        </div>
        {{ mode }}
    </div>
    <br>
    <Button @click="start">Start</Button>
    <Button @click="stop">Stop</Button>
    <Button @click="wordNumber++">add</Button>
    <Button @click="wordNumber=text.length-1">last</Button>
    <div>
        <span v-for="word, index in text"
            v-bind:key="word"
            class="text"
        ><span
            :class="{ under : index == wordNumber && started }"
        >{{ word }}</span>&nbsp;
        </span>
    </div>

    <InputText type="text" v-model="inText" @keypress.space="next" @keypress="press($event)" />
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
</div>
</template>

<script>
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'


import axios from 'axios'
export default {
    components: {
        Button,
        InputText,
        
    },
    title() {
        return "Writing Page"
    },
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

                    const randText = Math.floor( Math.random() * data.text.length )
                    const randMusic = Math.floor( Math.random() * data.music.length )
                    console.log(randText, randMusic)
                    this.text = data.text[ randText ].split(' ')
                    this.music = data.music[ randMusic ].split(' ')
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
                    if (this.music[currentNote] !== '*' && this.music[currentNote] !== '-') {
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
        },
        async win() {
            if (this.win === 1) {
                try {
                    await axios.put(`/api/users/${localStorage.getItem("usernameW")}`, {
                        bestSpeed: (this.lettersCount * 60000 / this.elapsedTime).toFixed(2)
                    }).then((response) => {
                        console.log(response.data)
                    })
                } catch (error) {
                    console.log(error.response)
                }
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