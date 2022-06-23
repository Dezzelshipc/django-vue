<template>
  <div>
    <div>
      <!--            <div>-->
      <!--              <input type="radio" value=-2 v-model="musicTrack">-->
      <!--              <label>Без трека</label>-->

      <!--              <input type="radio" value=-1 v-model="musicTrack">-->
      <!--              <label>Случайный трек</label>-->

      <!--              <input type="radio" value=0 v-model="musicTrack">-->
      <!--              <label>Л.В. Бетховен - К Элизе</label>-->

      <!--              <input type="radio" value=1 v-model="musicTrack">-->
      <!--              <label>#1</label>-->

      <!--              <input type="radio" value=2 v-model="musicTrack">-->
      <!--              <label>Мелодия номер 2</label>-->

      <!--              <input type="radio" value=3 v-model="musicTrack">-->
      <!--              <label>Мелодия номер 3</label>-->
      <!--            </div>-->
      <div class="musicMode">
        <label>
          <input type="radio" name="options" autocomplete="off" value=-2
                 v-model="musicTrack">
          <div class="musicCard"><img
              src="data:image/png;base64,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"
              width="100"
              height="100" class="imageMode"><h5>mute</h5></div>
        </label>
        <label>
          <input type="radio" name="options" autocomplete="off" value=-1
                 v-model="musicTrack">
          <div class="musicCard"><img
              src="https://vsekidki.ru/uploads/posts/2016-07/1469367149_perspective-dice-six-faces-random.png"
              width="100"
              height="100" class="imageMode"><h5>random</h5></div>
        </label>
        <label>
          <input type="radio" name="options" autocomplete="off" value=0
                 v-model="musicTrack">
          <div class="musicCard"><img
              src="https://www.ie.edu/insights/wp-content/uploads/2021/01/Simon-Beethoven-3.jpg"
              width="100"
              height="100" class="imageMode"><h5>Beethoven</h5></div>
        </label>
        <label>
          <input type="radio" name="options" autocomplete="off" value=1
                 v-model="musicTrack">
          <div class="musicCard"><img
              src="https://images-na.ssl-images-amazon.com/images/I/61M3rDwh4qL.png"
              width="100"
              height="100" class="imageMode"><h5>Tetris</h5></div>
        </label>
        <label>
          <input type="radio" name="options" autocomplete="off" value=2
                 v-model="musicTrack">
          <div class="musicCard"><img
              src="https://at-cdn-s02.audiotool.com/2018/09/08/documents/05rov985c3/0/cover256x256-fee67db15ed245a9886ae054730f3b98.jpg"
              width="100"
              height="100" class="imageMode"><h5>death note</h5></div>
        </label>
      </div>
    </div>
    <br>
    <div class="switchMode">
      <h6>top 1000 <br> random words</h6>
      <InputSwitch v-model="checked"/>
      <h6>random text</h6>
    </div>
    <br>
    <br>
    <br>
    <!--    <div>-->
    <!--      <input type="radio" value=1 v-model="mode">-->
    <!--      <label>Случайный текст</label>-->

    <!--      <input type="radio" value=2 v-model="mode">-->
    <!--      <label>Топ 1000 слов в русском языке</label>-->
    <!--    </div>-->
    <h5>
        <span v-for="word, index in text"
              v-bind:key="word"
              class="text"
        ><span
            :class="{ under : index == wordNumber && started }"
        >{{ word }}</span>&nbsp;
        </span>
    </h5>
    <div class="inputString">
      <Button @click="start">Start</Button> <!-- not for dev -->
      <InputText type="text" v-model="inText" @keypress.space="next" @keypress="press($event)"/>
      <Button @click="stop">Stop</Button>
    </div>
    {{ formattedElapsedTime }} {{ elapsedTime }} {{ this.timer }}
    <br>
    <Button @click="wordNumber++">add</Button>
    <Button @click="wordNumber=text.length-1">last</Button>
    {{ inText }}
    <br>
    Сходится: {{ isCorrect }}
    <br>
    Длины слова: {{ this.started ? this.text[this.wordNumber].length : 0 }} Длина напечатанного: {{
      this.inText.length
    }}
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
import InputSwitch from 'primevue/inputswitch'


import axios from 'axios'

export default {
  components: {
    Button,
    InputText,
    InputSwitch,

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

      checked: false,
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

          const idMusic = this.musicTrack == -1 ? Math.floor(Math.random() * data.length) : this.musicTrack

          this.music = responseM.data[idMusic].split(' ')
        } else {
          this.music = []
        }

        if (this.checked == true) {
          const responseT = await axios.get('/api/assets/json/texts.json')

          const data = responseT.data

          const idText = Math.floor(Math.random() * data.length)
          this.text = data[idText].replace("—", "-").split(' ')
        } else if (this.checked == false) {
          const responseW = await axios.get('/api/assets/json/words.json')

          const data = responseW.data

          this.text = data.sort(() => 0.5 - Math.random()).slice(0, 30 + Math.floor(Math.random() * 5))
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
      return (this.elapsedTime < 0 ? "-" : '') + utc.substr(utc.indexOf(":") + 1, 8);
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
  margin-left: 10px;
  margin-right: 10px;
  margin-top: 8px;
  margin-bottom: 5px;
  pointer-events: none;
}

label > input{ /* HIDE RADIO */
  visibility: hidden; /* Makes input not-clickable */
  position: absolute; /* Remove input from document flow */
}
label > input + .musicCard{ /* IMAGE STYLES */
  transition: 0.15s;
  display: flex;
  flex-direction: column;
  padding: 5px;
  border-radius: 5px;
  cursor: pointer;
  background-color: rgba(103,59,183, .30);
  color: whitesmoke;
  border: 1px solid rgba(76, 76, 122, 0);
}
.musicCard:hover {
  border: 1px solid #2c3e50;;
}
label > input:checked + .musicCard{ /* (RADIO CHECKED) IMAGE STYLES */
  background-color: rgb(103,59,183);
}

/*.musicCard {*/
/*  transition: 0.15s;*/
/*  display: flex;*/
/*  flex-direction: column;*/
/*  padding: 5px;*/
/*  border-radius: 5px;*/
/*  cursor: pointer;*/
/*  background-color: rgba(103,59,183, .30);*/
/*  color: whitesmoke;*/
/*}*/
/*.musicCard:active {*/
/*  background: chartreuse;*/
/*}*/
/*.musicCard:hover {*/
/*  background-color: #e598ff;*/
/*}*/

/*.musicCard input {*/
/*  order: 2;*/
/*}*/

/*.musicCard label {*/
/*  order: 1;*/
/*}*/

/*input:checked + label {*/
/*  background-color: rgb(103,59,183);*/
/*}*/

.p-inputtext {
  background-color: rgba(255, 255, 255, .30);
  backdrop-filter: blur(5px);
}

.inputString {
  display: flex;
  justify-content: center;
}

.musicMode {
  display: flex;
  justify-content: space-evenly;
}
.switchMode {
  display: flex;
  justify-content: center;
  max-width: 400px;
  border-radius: 10px;
  margin-right: auto;
  margin-left: auto;
  background-color: rgba(103,59,183, .30);
  align-items: center;
  padding: 10px;
  color: whitesmoke;

}
.p-inputswitch {
  margin-left: 20px;
  margin-right: 20px;
}
.p-inputswitch .p-inputswitch-slider {
  background: #886DCD;
}
.p-inputswitch .p-inputswitch-slider:hover {
  background: aqua;
}
.p-inputswitch .p-inputswitch-slider:before {
  background: #673AB7;
}
</style>