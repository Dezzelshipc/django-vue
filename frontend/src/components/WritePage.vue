<template>
<div>
  <div>
    <div>
        <input type="radio" value=1 v-model="mode">
        <label>Случайный текст</label>

        <input type="radio" value=2 v-model="mode">
        <label>Топ 1000 слов в русском языке</label>
    </div>
    <div>
        <input type="radio" value=-2 v-model="musicTrack">
        <label>Без трека</label>

        <input type="radio" value=-1 v-model="musicTrack">
        <label>Случайный трек</label>

        <input type="radio" value=0 v-model="musicTrack">
        <label>Л.В. Бетховен - К Элизе</label>
        
        <input type="radio" value=1 v-model="musicTrack">
        <label>#1</label>
        
        <input type="radio" value=2 v-model="musicTrack">
        <label>Мелодия номер 2</label>
        
        <input type="radio" value=3 v-model="musicTrack">
        <label>Мелодия номер 3</label>
    </div>
    <br>

    <input type="radio" class="btn-check" name="options" id="option1" autocomplete="off" value=-1 v-model="musicTrack">
    <label class="btn btn-dark" for="option1"><img src="https://vsekidki.ru/uploads/posts/2016-07/1469367149_perspective-dice-six-faces-random.png" width="100" height="100" class="imageMode"> </label>

    <input type="radio" class="btn-check" name="options" id="option2" autocomplete="off" checked value=0 v-model="musicTrack">
    <label class="btn btn-dark" for="option2"><img src="https://www.zvuki.ru/images/photo/64/64421.jpg" width="100" height="100" class="imageMode"> </label>

    <input type="radio" class="btn-check" name="options" id="option3" autocomplete="off" value=1 v-model="musicTrack">
    <label class="btn btn-dark" for="option3"><img src="https://i.imgur.com/eMfKGJG.jpg" width="100" height="100" class="imageMode"> </label>

    <input type="radio" class="btn-check" name="options" id="option4" autocomplete="off" value=2 v-model="musicTrack">
    <label class="btn btn-dark" for="option4"><img src="https://i.imgur.com/Ia0mmdp.jpg" width="100" height="100" class="imageMode"> </label>



  </div>

    <br>


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
    <Button @click="start">Start</Button> <!-- not for dev -->
    <InputText type="text" v-model="inText" @keypress.space="next" @keypress="press($event)" />
    <Button @click="stop">Stop</Button>
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
            musicTrack: -1,
            currentNote: 0,
        }
    },
    methods: {
        async start() {
            try {
                this.inText = ''
                this.elapsedTime = -3000
                this.wordNumber = 0
                this.currentNote = 0

                this.lettersCount = 0

                if (this.musicTrack != -2) {
                    const responseM = await axios.get('/api/assets/json/music.json')

                    const data = responseM.data

                    const idMusic = this.musicTrack == -1 ? Math.floor( Math.random() * data.length ) : this.musicTrack

                    this.music = responseM.data[ idMusic ].split(' ')
                } else {
                    this.music = []
                }

                if (this.mode == 1) {
                    const responseT = await axios.get('/api/assets/json/texts.json')

                    const data = responseT.data
                    
                    const idText = Math.floor( Math.random() * data.length )
                    this.text = data[ idText ].replace("—", "-").split(' ')
                } else if (this.mode == 2) {
                    const responseW = await axios.get('/api/assets/json/words.json')

                    const data = responseW.data
                    
                    this.text = data.sort(() => 0.5 - Math.random()).slice(0, 30 + Math.floor( Math.random() * 5))
                }
                this.started = 1;

                (new Audio(`/api/assets/audio/count_down.mp3`)).play()
                
                if (!this.timer) {
                    this.timer = setInterval(() => {
                        this.elapsedTime += 10
                    }, 10)
                }
            } catch (error) {
                console.log(error)
                this.text = ['Server', 'error']
            }
        },
        next(event) {
            if (this.isCorrect && this.text[this.wordNumber].length === this.inText.length) {
                event.preventDefault()
                this.inText = ''
                this.playNext()
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
            this.started = 0
        },
        reset() {
            this.elapsedTime = 0;
        },
        press(event) {
            if (this.elapsedTime < 0 || this.timer === undefined) {
                event.preventDefault()
            } else {
                this.lettersCount++
                
                if (this.isCorrect && this.music.length && this.text[this.wordNumber].startsWith(this.inText.trim() + event.key)) {
                    this.playNext()
                }
            }
        },
        playNext() {
            this.currentNote = (this.currentNote + 1) % this.music.length
            if (this.music[this.currentNote] !== '*' && this.music[this.currentNote] !== '-') {
                let audio = new Audio(`/api/assets/audio/notes_${this.music[this.currentNote]}.mp3`)
                audio.play()
            }
        }
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
.imageMode {
  border-radius: 5px;
}
</style>