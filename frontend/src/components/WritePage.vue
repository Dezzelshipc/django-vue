<template>
<div>
    <button @click="start">Start</button>
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
    
    <input type="text" v-model="inText" @keypress.space="next" @keypress="(event) => { (elapsedTime < 0) ? event.preventDefault() : '' }">
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
    Знаков в минуту: {{ (lettersCount * 60000 / elapsedTime).toFixed(2) }}
</div>
</template>

<script>
import { ref } from 'vue'

export default {
    data() {
        return {
            inText: ref(''),
            started: ref(0),
            wordNumber: ref(0),
            text: ref([]),
            win: ref(0),
            miss: ref(0),
            lettersCount: ref(0),

            elapsedTime: ref(-3000),
            timer: ref(undefined),
        }
    },
    methods: {
        start() {
            this.inText = ''
            this.elapsedTime = -3000
            this.wordNumber = 0
            let text = "Сосны обступали тропу плотно, и, хотя истыканное их верхушками небо светилось голубым, в лесу было сумрачно. По тропинке вперёд бежали муравьи, большие, красные, по своим каким-то муравьиным делам.";
            this.lettersCount = text.length
            this.text = text.split(' ')
            this.started = 1;

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