<template>
  <div>
    <h2>
      Добро пожаловать на сайт, где вы можете тренировать скорость печати, при этом играя музыку, которую вы выберете, или случайную!
    </h2>
    <h2>
      Если вы хотите получать оповещения о рекордах какого-то пользователя, вы можете сделать это с помощью телеграм бота: <a href="https://t.me/DjangoVueProjBot">@DjangoVueProjBot</a>
    </h2>
    <img src="@/assets/img/spaceman.png" class="spaceman">
  </div>
</template>

<script>
export default {
  methods: {
    
  },
  title() {
    return "Home"
  },
}
</script>

<style>
.spaceman {
  margin-top: 20px;
  height: 225px;
  width: 225px;
  margin-right: auto;
  margin-left: auto;
}
</style>