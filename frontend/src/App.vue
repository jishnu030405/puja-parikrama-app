<template>
  <div class="app">
    <div class="top-border"></div>

    <!-- ================= NAVBAR ================= -->

    <header class="navbar">
      <div class="nav-inner container">

        <a href="#home" class="brand">
          <img
            src="/durga-eye.png"
            alt="Maa Durga"
            class="durga-eye"
          />

          <span>Pujo Parikrama 2026</span>
        </a>

        <nav>
          <select 
            class="form-select"
            aria-label="Choose City"
            style="width: 150px; border: 2px solid #8b0000; border-radius: 14px; padding: 2px 20px; font-size: 16px; background-color: #fff8ed; color: #5a1a1a; outline:none;box-shadow: none;"
          >
            <option selected>Choose City</option>
            <option value="1">Durgapur</option>
          </select>
          <a href="#pandals">Top Pandals</a>
          <a href="#route-planner">Route Planner</a>
          <a href="/review">Review</a>
      
        </nav>

        <button
          class="menu-button"
          type="button"
          @click="menuOpen = !menuOpen"
        >
          ☰
        </button>

      </div>

      <div v-if="menuOpen" class="mobile-menu">

        <a
          href="#pandals"
          @click="menuOpen = false"
        >
          Top Pandals
        </a>

        <a
          href="#route-planner"
          @click="menuOpen = false"
        >
          Route Planner
        </a>

      <a
        href="/review"
        @click="menuOpen = false"
        >
        Review
    </a>

      </div>
    </header>


    <main>

      <!-- ================= HERO ================= -->

      <section id="home" class="hero">

        <div class="hero-copy">

          <div class="decorated-title">

            <span class="flower">✤</span>

            <span class="line"></span>

            <span class="lotus">✿</span>

            <h1>জয় মা দুর্গা</h1>

            <span class="lotus">✿</span>

            <span class="line"></span>

            <span class="flower">✤</span>

          </div>
          <h5 style="color: #9B111E; font-family: Georgia, serif; font-size: 16px; font-weight: 500; line-height: 1.7; text-align: center; margin: 12px 0 16px; opacity: 0.9;">🪷 যা দেবী সর্বভূতেষু শক্তিরূপেণ সংস্থিতা।<br>
            নমস্তস্যৈ নমস্তস্যৈ নমস্তস্যৈ নমো নমঃ॥ 🪷</h5>




          <h2>Experience the Divine</h2>


          <p class="hero-description">
            Discover All Durgapur Durga Pujo pandels,
            explore the best pandels,<br
              class="desktop-only"
            />
            and navigate directly from your location.
            <br>
            <br>
          </p>
          
          <!-- COUNTDOWN -->

          <div class="countdown-section">

            <div class="countdown-title">
             {{ pujaDay }}
            </div>


            <div
              v-if="showCountdown"
              class="countdown"
            >

              <div class="time-box">
                <strong>{{ days }}</strong>
                <small>Days</small>
              </div>

              <div class="time-box">
                <strong>{{ hours }}</strong>
                <small>Hours</small>
              </div>

              <div class="time-box">
                <strong>{{ minutes }}</strong>
                <small>Minutes</small>
              </div>

              <div class="time-box">
                <strong>{{ seconds }}</strong>
                <small>Seconds</small>
              </div>

            </div>

          </div>


          <!-- HERO BUTTON -->

          <div class="hero-actions">

            <a
              href="#pandals"
              class="hero-btn primary"
            >
              ⌖
              <span>Find Pandals</span>
              →
            </a>

          </div>


          <p class="location-status">
            {{ locationStatusText }}
          </p>

        </div>


        <div class="hero-image-wrap">

          <img
            src="/durga-portrait.jpg"
            alt="Maa Durga"
            class="hero-image"
          />

        </div>

      </section>


      <!-- ================= PANDALS ================= -->

      <section
        id="pandals"
        class="section pandal-section"
      >

        <div class="container">

          <div class="section-heading">

            <p class="eyebrow">
              DURGAPUR DURGA PUJO 2026
            </p>

            <h2>Top Pandels</h2>

            <p>
              Explore Durgapur Durga Pujo pandels
              and navigate directly from your
              current location.
            </p>

          </div>
          <p style="text-align:center;font-size:13px;color:#7a4b20;margin:12px 0;opacity:0.85;">For the best viewing experience, switch to Desktop Site.</p>

          <!-- SEARCH -->

          <div class="search-box">

            <span>⌕</span>

            <input
              v-model="searchQuery"
              type="search"
              placeholder="Search a pandel..."
            />

          </div>
        </div>


          <!-- PANDAL GRID -->
          
          <div class="pandal-grid">

            <article 
              v-for="pandal in filteredPandals.slice(0, visiblePandalCount)" 
              :key="pandal.id" 
              class="pandal-card" 
            >

              <div class="card-number">

                {{
                  String(pandal.id)
                    .replace('pandal-', '')
                    .padStart(2, '0')
                }}

              </div>


              <div class="card-content">

                <h3>
                  {{ pandal.name }}
                </h3>


                <p>
                  📍 {{ pandal.location }}
                </p>


                <span class="zone">
                  {{ pandal.zone }}
                </span>


                <span class="zone">
                  {{ pandal.tags[0] }}
                </span>


                <!-- NAVIGATION -->

                <button 
                  class="text-button" 
                  type="button" 
                  :disabled="activePandalId === pandal.id" 
                  @click="goToPandal(pandal)" 
                >
                  {{ pandalButtonLabel(pandal) }}
                </button>

              </div>

            </article>

          </div>


          <!-- SHOW MORE / SHOW LESS -->

          <div
            v-if="filteredPandals.length > 6"
            style="text-align: center; margin-top: 25px;"
          >

            <button
              type="button"
              @click="
                visiblePandalCount < filteredPandals.length
                  ? visiblePandalCount = Math.min(
                      visiblePandalCount + 6,
                      filteredPandals.length
                    )
                  : visiblePandalCount = 6
              "
              style="
                padding: 10px 22px;
                border: 2px solid #8b0000;
                border-radius: 20px;
                background: #fff8ed;
                color: #8b0000;
                font-size: 15px;
                font-weight: 600;
                cursor: pointer;
              "
            >

              {{
                visiblePandalCount < filteredPandals.length
                  ? '▼ Show More'
                  : '▲ Show Less'
              }}

            </button>

          </div>


          <!-- NO RESULTS -->

          <p 
            v-if="filteredPandals.length === 0" 
            class="empty" 
          >
            No predefined pandal found. 
          </p>
          


          
      </section>


      <!-- ROUTE PLANNER  -->

      <section
        id="route-planner"
        class="section route-planner-section"
      >

        <div class="container">

          <div class="section-heading">

            <p class="eyebrow">
              PLAN YOUR PARIKRAMA
            </p>

            <h2>Route Planner</h2>

            <p>
              Tell us which side of town you're
              coming in from, and we'll order every
              pandel from nearest to farthest, so you
              always know what's next.
            </p>

          </div>


          <!-- SIDE PICKER -->

          <div class="route-start-picker">

            <button
              v-for="start in ROUTE_PLANNER_STARTS"
              :key="start.id"
              type="button"
              class="route-start-option"
              :class="{ active: selectedRouteStartId === start.id }"
              @click="selectRouteStart(start.id)"
            >

              <span class="route-start-icon">
                {{ start.icon }}
              </span>

              <span class="route-start-text">

                <strong>{{ start.label }}</strong>

                <small>{{ start.description }}</small>

              </span>

            </button>

          </div>


          <!-- SORTED PANDAL LIST -->

          <div
            v-if="selectedRouteStart"
            class="route-pandal-list"
          >

            <article
              v-for="(pandal, index) in routePlannerPandals"
              :key="pandal.id"
              class="route-pandal-card"
            >

              <div class="route-pandal-rank">
                {{ index + 1 }}
              </div>


              <div class="route-pandal-info">

                <h3>{{ pandal.name }}</h3>

                <p>📍 {{ pandal.location }}</p>

                <span class="zone">
                  {{ pandal.zone }}
                </span>

                <span class="route-pandal-distance">
                  ~{{ pandal.distanceKm.toFixed(1) }} km
                  {{
                    index === 0
                      ? `from ${selectedRouteStart.label.replace('From ', '')}`
                      : 'from the previous stop'
                  }}
                </span>

                <button
                  class="text-button"
                  type="button"
                  :disabled="activePandalId === pandal.id"
                  @click="goToPandal(pandal)"
                >
                  {{ pandalButtonLabel(pandal) }}
                </button>

              </div>

            </article>

          </div>


          <p
            v-else
            class="empty"
          >
            Pick a side above to see pandels ordered
            nearest to farthest.
          </p>

        </div>

      </section>


      <!-- ================= TOILETS ================= -->
        <section id="facilities" class="section toilet-section">

  <div class="container">

    <div class="facility-grid">

      <div class="toilet-card">

        <div>
          <p class="eyebrow">
            QUICK HELP
          </p>

          <h2>
            🚻 Toilet Finder
          </h2>

          <p>
            Find nearby public toilets using your current location.
          </p>
        </div>

        <button
          class="hero-btn primary"
          type="button"
          @click="findToilets"
        >
          Find Nearby Toilets
        </button>

      </div>


      <div class="toilet-card">

        <div>
          <p class="eyebrow">
            QUICK HELP
          </p>

          <h2>
            🏥 Nearby Hospitals
          </h2>

          <p>
            Find nearby hospitals using your current location.
          </p>
        </div>

        <button
          class="hero-btn primary"
          type="button"
          @click="findHospitals"
        >
          Find Nearby Hospitals
        </button>

      </div>

    </div>

  </div>

</section>
      
      

    </main>


    <!-- ================= FOOTER ================= -->

    <footer class="app-footer">

      <div class="bottom-border"></div>


      <div class="container footer-content">

        <div class="footer-about">

          <h3>
            🪔 Pujo Parikrama 2026
          </h3>

          <p>
            Your simple companion for exploring
            Durga Puja pandels across Durgapur.
          </p>

        </div>


        <div class="footer-links">

          <h4>
            Explore
          </h4>

          <a href="#home">
            Home
          </a>

          <a href="#pandals">
            Top Pandels
          </a>

          <a href="#route-planner">
            Route Planner
          </a>
          
          <a href="/review">
            Review
          </a>


        </div>


        <div class="footer-puja">

          <h4>
            দুর্গাপূজা ২০২৬
          </h4>

          <p>

            Made For Durgapur only
          </p>


        </div>

      </div>


      <div class="footer-bottom">

        <div class="container">

          <span>
            © 2026 Pujo Parikrama • Designed & Developed by Jishnujit Mete
          </span>

          <span>
            Made with devotion for Maa Durga ❤️
          </span>

        </div>

      </div>

    </footer>

  </div>
</template>


<script setup>

import {
  computed,
  onMounted,
  onUnmounted,
  ref
} from 'vue'

import {
  initialDurgapurPandals
} from './data/pandals.js'



// BASIC STATE
const visiblePandalCount = ref(6)

const searchQuery = ref('')

const menuOpen = ref(false)

const days = ref(0)

const hours = ref(0)

const minutes = ref(0)

const seconds = ref(0)



// LIVE LOCATION STATE
//
// This holds the user's most recently known GPS position.
// It is refreshed:
//   - once when the app first opens
//   - automatically whenever the user returns to the app
//     (e.g. after visiting a pandal and switching back)
//   - right before every "Go to Pandal" navigation
//
// It should NEVER be assumed to still be "at the last pandal" -
// it always reflects the latest real GPS reading.


const currentLocation = ref(null) // { lat, lng, accuracy, timestamp }

// 'idle' | 'locating' | 'ready' | 'denied' | 'unavailable' | 'error'
const locationStatus = ref('idle')



// LOCATION STATUS TEXT (for the small indicator in the hero)


const locationStatusText =
  computed(() => {

    switch (locationStatus.value) {

      case 'locating':
        return '📍 Getting your live location...'

      case 'ready':
        return '📍 Live location ready — routes start from where you are now'

      case 'denied':
        return '📍 Location permission denied — enable it to auto-start routes from where you are'

      case 'unavailable':
        return '📍 Location unavailable — please turn on GPS'

      case 'error':
        return '📍 Could not get your location — will retry when you pick a pandal'

      default:
        return '📍 Location not yet requested'

    }

  })



// ROUTE PLANNER

const ROUTE_PLANNER_STARTS = [
  {
    id: 'asansol',
    label: 'From Asansol Side',
    description: 'Entering Durgapur via GT Road from Asansol',
    icon: '🚏',
    lat: 23.69131,
    lng: 86.974792
  },
  {
    id: 'durgapur-station',
    label: 'From Durgapur Station Side',
    description: 'Entering from Durgapur Railway Station',
    icon: '🚉',
    lat: 23.494747481750085,
    lng: 87.31900335338192
  }
]

// id of the side the user picked, or null if none picked yet
const selectedRouteStartId = ref(null)

const selectedRouteStart =
  computed(() =>
    ROUTE_PLANNER_STARTS.find(
      (start) => start.id === selectedRouteStartId.value
    ) || null
  )

function selectRouteStart(startId) {

  selectedRouteStartId.value =
    selectedRouteStartId.value === startId
      ? null // tapping the same option again clears the selection
      : startId

}


// ------------------------------------------------------------
// Haversine distance between two lat/lng points, in kilometers.
// Straight-line distance, not a road route - used to decide
// which pandal is "nearest" at each step of route-building.
// ------------------------------------------------------------

function toRadians(degrees) {
  return degrees * (Math.PI / 180)
}

function distanceInKm(lat1, lng1, lat2, lng2) {

  const EARTH_RADIUS_KM = 6371

  const dLat =
    toRadians(lat2 - lat1)

  const dLng =
    toRadians(lng2 - lng1)

  const a =

    Math.sin(dLat / 2) * Math.sin(dLat / 2) +

    Math.cos(toRadians(lat1)) *
    Math.cos(toRadians(lat2)) *
    Math.sin(dLng / 2) * Math.sin(dLng / 2)

  const c =
    2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))

  return EARTH_RADIUS_KM * c

}


// ------------------------------------------------------------
// Nearest-neighbor route builder.
//
// Starting from (startLat, startLng), repeatedly picks whichever
// REMAINING pandal is closest to the last pandal added to the
// route (for the very first pick, "last pandal" is the starting
// point itself). Each result also carries `distanceKm`, the hop
// distance from the previous stop (or from the start, for #1).
// ------------------------------------------------------------

function buildNearestNeighborRoute(startLat, startLng, pandals) {

  const remaining = [...pandals]
  const route = []

  let fromLat = startLat
  let fromLng = startLng

  while (remaining.length > 0) {

    let nearestIndex = 0
    let nearestDistance = Infinity

    remaining.forEach((pandal, index) => {

      const distance = distanceInKm(
        fromLat,
        fromLng,
        pandal.lat,
        pandal.lng
      )

      if (distance < nearestDistance) {
        nearestDistance = distance
        nearestIndex = index
      }

    })

    const [nextPandal] =
      remaining.splice(nearestIndex, 1)

    route.push(nextPandal)

    fromLat = nextPandal.lat
    fromLng = nextPandal.lng

  }

  return route

}


// ------------------------------------------------------------
// Total length (km) of a route starting at (startLat, startLng)
// and visiting each pandal in order.
// ------------------------------------------------------------

function totalRouteDistanceKm(startLat, startLng, route) {

  let total = 0
  let fromLat = startLat
  let fromLng = startLng

  for (const pandal of route) {

    total += distanceInKm(fromLat, fromLng, pandal.lat, pandal.lng)

    fromLat = pandal.lat
    fromLng = pandal.lng

  }

  return total

}



// 2-opt improvement pass.


function twoOptOptimize(startLat, startLng, route) {

  let best = [...route]
  let improved = true

  while (improved) {

    improved = false

    for (let i = 1; i < best.length - 1; i++) {

      for (let j = i + 1; j < best.length; j++) {

        const candidate = [
          ...best.slice(0, i),
          ...best.slice(i, j + 1).reverse(),
          ...best.slice(j + 1)
        ]

        const candidateDistance =
          totalRouteDistanceKm(startLat, startLng, candidate)

        const bestDistance =
          totalRouteDistanceKm(startLat, startLng, best)

        if (candidateDistance < bestDistance - 1e-9) {
          best = candidate
          improved = true
        }

      }

    }

  }

  return best

}


// Builds the final route: nearest-neighbor construction, then
// straightened out with 2-opt, then re-attaches each stop's hop
// distance (from the previous stop, or from the start for #1)
// for display.

function buildRoute(startLat, startLng, pandals) {

  const initialRoute =
    buildNearestNeighborRoute(startLat, startLng, pandals)

  const optimizedRoute =
    twoOptOptimize(startLat, startLng, initialRoute)

  let fromLat = startLat
  let fromLng = startLng

  return optimizedRoute.map((pandal) => {

    const distanceKm =
      distanceInKm(fromLat, fromLng, pandal.lat, pandal.lng)

    fromLat = pandal.lat
    fromLng = pandal.lng

    return { ...pandal, distanceKm }

  })

}


// The route for whichever side is currently selected.

const routePlannerPandals =
  computed(() => {

    if (!selectedRouteStart.value) {
      return []
    }

    const start = selectedRouteStart.value

    return buildRoute(
      start.lat,
      start.lng,
      initialDurgapurPandals
    )

  })


// ============================================================
// FILTER PANDALS
// ============================================================

const filteredPandals =
  computed(() => {

    const query =
      searchQuery.value
        .trim()
        .toLowerCase()


    return initialDurgapurPandals.filter(
      (pandal) =>
        `${pandal.name} ${pandal.location} ${pandal.zone}`
          .toLowerCase()
          .includes(query)
    )

  })


// ============================================================
// COUNTDOWN DISPLAY
// ============================================================

const showCountdown =
  computed(() => {

    const currentDate =
      new Date()


    const year =
      currentDate.getFullYear()

    const month =
      currentDate.getMonth()

    const date =
      currentDate.getDate()


    return (

      year === 2026 &&

      (
        month === 8 ||

        (
          month === 9 &&
          date <= 13
        )
      )

    )

  })



// PUJA DAY

const pujaDay =
  computed(() => {

    const currentDate =
      new Date()


    const year =
      currentDate.getFullYear()

    const month =
      currentDate.getMonth()

    const date =
      currentDate.getDate()


    if (
      year === 2026 &&
      (
        month === 8 ||
        (
          month === 9 &&
          date <= 13
        )
      )
    ) {

      return 'মা আসছেন'

    }


    if (
      year === 2026 &&
      month === 9 &&
      date === 14
    ) {

      return 'মহা চতুর্থী'

    }


    if (
      year === 2026 &&
      month === 9 &&
      date === 15
    ) {

      return 'মহা পঞ্চমী'

    }


    if (
      year === 2026 &&
      month === 9 &&
      date === 16
    ) {

      return 'মহা ষষ্ঠী'

    }


    if (
      year === 2026 &&
      month === 9 &&
      date === 17
    ) {

      return 'মহা সপ্তমী'

    }


    if (
      year === 2026 &&
      month === 9 &&
      date === 18
    ) {

      return 'মহা অষ্টমী'

    }


    if (
      year === 2026 &&
      month === 9 &&
      date === 19
    ) {

      return 'মহা অষ্টমী'

    }


    if (
      year === 2026 &&
      month === 9 &&
      date === 20
    ) {

      return 'মহা নবমী'

    }


    if (
      year === 2026 &&
      month === 9 &&
      date === 21
    ) {

      return 'বিজয়া দশমী'

    }


    return 'শুভ বিজয়া'

  })



// COUNTDOWN


function updateCountdown() {

  const currentDate =
    new Date()


  const targetDate =
    new Date(
      '2026-10-14T00:00:00'
    )


  const difference =
    targetDate -
    currentDate


  if (difference <= 0) {

    days.value = 0

    hours.value = 0

    minutes.value = 0

    seconds.value = 0

    return

  }


  days.value =
    Math.floor(
      difference /
      (1000 * 60 * 60 * 24)
    )


  hours.value =
    Math.floor(
      (
        difference /
        (1000 * 60 * 60)
      ) % 24
    )


  minutes.value =
    Math.floor(
      (
        difference /
        (1000 * 60)
      ) % 60
    )


  seconds.value =
    Math.floor(
      (
        difference /
        1000
      ) % 60
    )

}



// GOOGLE MAPS

function openGoogleMaps(url) {

  window.location.href = url

}



// ============================================================

function getFreshLocation() {

  return new Promise((resolve, reject) => {

    if (!navigator.geolocation) {

      locationStatus.value = 'unavailable'

      reject(new Error('unsupported'))

      return

    }

    locationStatus.value = 'locating'

    navigator.geolocation.getCurrentPosition(

      (position) => {

        const latitude =
          position.coords.latitude

        const longitude =
          position.coords.longitude

        const accuracy =
          position.coords.accuracy


        console.log(
          '========== CURRENT LOCATION =========='
        )

        console.log('Latitude:', latitude)
        console.log('Longitude:', longitude)
        console.log('Accuracy:', `${Math.round(accuracy)} meters`)

        console.log(
          '======================================='
        )


        currentLocation.value = {
          lat: latitude,
          lng: longitude,
          accuracy,
          timestamp: Date.now()
        }

        locationStatus.value = 'ready'

        resolve(currentLocation.value)

      },


      (error) => {

        console.error('Geolocation error:', error)

        if (error.code === error.PERMISSION_DENIED) {
          locationStatus.value = 'denied'
        } else if (error.code === error.POSITION_UNAVAILABLE) {
          locationStatus.value = 'unavailable'
        } else {
          locationStatus.value = 'error'
        }

        reject(error)

      },


      {
        enableHighAccuracy: true,
        timeout: 20000,
        maximumAge: 0 // never reuse a cached/stale fix
      }

    )

  })

}


function showLocationErrorAlert(error) {

  if (error && error.message === 'unsupported') {

    alert('Location access is not supported by your browser.')
    return

  }

  if (error && error.code === error.PERMISSION_DENIED) {

    alert(
      'Location permission was denied. Please allow location access for this website in your phone settings.'
    )

  } else if (error && error.code === error.POSITION_UNAVAILABLE) {

    alert(
      'Your phone could not determine your current location. Please turn on Location/GPS and try again.'
    )

  } else if (error && error.code === error.TIMEOUT) {

    alert(
      'Getting your location took too long. Please try again.'
    )

  } else {

    alert(
      'Unable to get your current location. Please try again.'
    )

  }

}



const MAX_LOCATION_AGE_MS = 2 * 60 * 1000 // 2 minutes


const activePandalId = ref(null)
const activePandalPhase = ref('')

function isLocationFreshEnough(location) {

  return (
    location &&
    (Date.now() - location.timestamp) < MAX_LOCATION_AGE_MS
  )

}

async function goToPandal(pandal) {

  activePandalId.value = pandal.id

  let location = currentLocation.value

  if (!isLocationFreshEnough(location)) {

    

    activePandalPhase.value = 'locating'

    try {

      location = await getFreshLocation()

    } catch (error) {

      showLocationErrorAlert(error)
      activePandalId.value = null
      activePandalPhase.value = ''
      return

    }

  }


  const origin =
    `${location.lat},${location.lng}`

  const destination =
    `${pandal.lat},${pandal.lng}`

  console.log('Origin (live GPS):', origin)
  console.log('Destination:', destination)


  const mapsUrl =
    `https://www.google.com/maps/dir/?api=1` +
    `&origin=${encodeURIComponent(origin)}` +
    `&destination=${encodeURIComponent(destination)}` +
    `&travelmode=driving`


  

  activePandalPhase.value = 'opening'

  openGoogleMaps(mapsUrl)


  
  silentlyRefreshLocation()

}


function pandalButtonLabel(pandal) {

  if (activePandalId.value !== pandal.id) {
    return 'Go to this pandal →'
  }

  if (activePandalPhase.value === 'locating') {
    return 'Locating...'
  }

  if (activePandalPhase.value === 'opening') {
    return 'Opening Maps...'
  }

  return 'Go to this pandal →'

}



// TOILET FINDER

function findToilets() {

  if (!navigator.geolocation) {

    openGoogleMaps(
      'https://www.google.com/maps/search/?api=1&query=public+toilet+near+me'
    )

    return

  }


  navigator.geolocation.getCurrentPosition(

    (position) => {

      const location =
        `${position.coords.latitude},${position.coords.longitude}`


      openGoogleMaps(

        `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(
          `public toilets near ${location}`
        )}`

      )

    },


    () => {

      openGoogleMaps(
        'https://www.google.com/maps/search/?api=1&query=public+toilet+near+me'
      )

    },


    {
      enableHighAccuracy: true,
      timeout: 8000,
      maximumAge: 60000
    }

  )

}

// Hospital finder
function findHospitals() {

  if (!navigator.geolocation) {

    openGoogleMaps(
      'https://www.google.com/maps/search/?api=1&query=hospitals+near+me'
    )

    return

  }


  navigator.geolocation.getCurrentPosition(

    (position) => {

      const location =
        `${position.coords.latitude},${position.coords.longitude}`


      openGoogleMaps(

        `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(
          `hospitals near ${location}`
        )}`

      )

    },


    () => {

      openGoogleMaps(
        'https://www.google.com/maps/search/?api=1&query=hospitals+near+me'
      )

    },


    {
      enableHighAccuracy: true,
      timeout: 8000,
      maximumAge: 60000
    }

  )

}






// LIFECYCLE


let countdownTimer = null




function silentlyRefreshLocation() {

  getFreshLocation().catch(() => {
    // Ignored here - goToPandal() will retry (and alert if needed)
    // the moment the user actually taps a pandal.
  })

}


// ------------------------------------------------------------
// Fires when the user switches back to this tab/app - e.g.
// after visiting Pandal A in Google Maps and returning here.
// Re-fetches GPS immediately so we never keep treating the
// previous pandal (or wherever they wandered off to) as "current".


function handleVisibilityChange() {

  if (document.visibilityState === 'visible') {

    silentlyRefreshLocation()

  }

}


onMounted(() => {

  updateCountdown()

  countdownTimer =
    setInterval(
      updateCountdown,
      1000
    )


  // 1. Get the user's location as soon as the app opens

  silentlyRefreshLocation()


  // 2. Keep it fresh whenever they return to the app

  document.addEventListener(
    'visibilitychange',
    handleVisibilityChange
  )

  window.addEventListener(
    'focus',
    handleVisibilityChange
  )

})


onUnmounted(() => {

  clearInterval(countdownTimer)

  document.removeEventListener(
    'visibilitychange',
    handleVisibilityChange
  )

  window.removeEventListener(
    'focus',
    handleVisibilityChange
  )

})

</script>


<style scoped>

:global(*) {
  box-sizing: border-box;
}

:global(html) {
  scroll-behavior: smooth;
}

.app {
  min-height: 100vh;
  background: #fff9ed;
  color: #321b15;
}

.container {
  width: min(1120px, calc(100% - 40px));
  margin: 0 auto;
}

.top-border {
  height: 9px;
  background: #8e0d18 url('/top-border.jpg') center / auto 22px repeat-x;
}


/* ================= NAVBAR ================= */

.navbar {
  position: sticky;
  top: 0;
  z-index: 20;
  background: rgba(255, 249, 237, .97);
  border-bottom: 1px solid #e7cda2;
  box-shadow: 0 3px 12px rgba(90, 30, 20, .08);
}

.nav-inner {
  min-height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  color: #8c0b17;
  font: 700 1.25rem Georgia, serif;
}

.durga-eye {
  width: 34px;
  height: 34px;
  object-fit: contain;
}

nav {
  display: flex;
  align-items: center;
  gap: 30px;
}

nav a {
  position: relative;
  color: #4c2922;
  font: 600 .88rem Georgia, serif;
}

nav a:hover {
  color: #9c101b;
}

.menu-button {
  display: none;
  color: #8c0b17;
  font-size: 1.35rem;
}

.mobile-menu {
  display: none;
}


/* ================= HERO ================= */

.hero {
  position: relative;
  min-height: 540px;
  display: grid;
  grid-template-columns: 53% 47%;
  overflow: hidden;
 
  /* Single shared background behind both columns so the image
     dissolves into it with no visible seam */
  background:
    radial-gradient(
      circle at 32% 45%,
      rgba(255, 255, 255, 0.4),
      transparent 55%
    ),
    linear-gradient(
      110deg,
      #fff4dc 0%,
      #f9e4bb 45%,
      #f3cf95 70%,
      #edc27f 100%
    );
}
 
.hero-copy {
  position: relative;
  z-index: 2;
  padding: 54px 38px 50px 8%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  /* no background here — .hero's shared background shows through */
}
 
.hero-image-wrap {
  min-height: 540px;
  position: relative;
  overflow: hidden;
  /* no background here either — lets .hero show through the mask fade */
}
 
.hero-image {
  width: 100%;
  height: 100%;
  min-height: 540px;
  object-fit: cover;
  object-position: center;
  display: block;
 
  /* Top / right / bottom stay hard photo edges — only the LEFT edge
     dissolves, wide and soft, into the shared .hero background */
  -webkit-mask-image: linear-gradient(
    90deg,
    transparent 0%,
    rgba(0, 0, 0, 0.12) 10%,
    rgba(0, 0, 0, 0.35) 18%,
    rgba(0, 0, 0, 0.65) 26%,
    rgba(0, 0, 0, 0.88) 33%,
    #000 42%
  );
  mask-image: linear-gradient(
    90deg,
    transparent 0%,
    rgba(0, 0, 0, 0.12) 10%,
    rgba(0, 0, 0, 0.35) 18%,
    rgba(0, 0, 0, 0.65) 26%,
    rgba(0, 0, 0, 0.88) 33%,
    #000 42%
  );
  -webkit-mask-size: 100% 100%;
  mask-size: 100% 100%;
}


/* ================= HERO TITLE ================= */

.decorated-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: #a50d1a;
  margin-bottom: 5px;
}

.decorated-title h1 {
  margin: 0;
  font-family: Georgia, 'Noto Serif Bengali', serif;
  font-size: clamp(3rem, 5vw, 4.5rem);
  line-height: 1;
  font-weight: 800;
  color: #9f0d18;
  letter-spacing: -.04em;
}

.decorated-title .line {
  width: 46px;
  height: 1px;
  background: #9f0d18;
}

.decorated-title .flower {
  font-size: 1.6rem;
}

.decorated-title .lotus {
  font-size: 1.5rem;
  color: #9f0d18;
}

.hero-copy h2 {
  margin: 12px 0 4px;
  font: 700 clamp(1.7rem, 3vw, 2.3rem) Georgia, serif;
  color: #321b15;
}

.hero-description {
  color: #5e4338;
  font: .92rem/1.55 Georgia, serif;
  max-width: 450px;
}


/* ================= COUNTDOWN ================= */

.countdown-section {
  margin: 13px 0 14px;
  min-height: 66px;
}

.countdown-title {
  color: #9f0d18;
  font: 700 1.05rem Georgia, serif;
  margin-bottom: 7px;
}

.countdown {
  display: flex;
  justify-content: center;
  gap: 7px;
}

.time-box {
  min-width: 55px;
  padding: 5px 7px;
  border: 1px solid #dfbf87;
  border-radius: 8px;
  background: rgba(255, 250, 236, .72);
}

.time-box strong,
.time-box small {
  display: block;
}

.time-box strong {
  color: #8e0d18;
  font: 700 1.1rem Georgia, serif;
}

.time-box small {
  color: #76594d;
  font-size: .62rem;
  text-transform: uppercase;
  letter-spacing: .04em;
}


/* ================= BUTTONS ================= */

.hero-actions {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
}

.location-status {
  margin-top: 10px;
  color: #8b6714;
  font: 600 .75rem Georgia, serif;
}

.hero-btn {
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 0 21px;
  border-radius: 999px;
  font: 700 .88rem Georgia, serif;
  transition:
    transform .18s ease,
    box-shadow .18s ease;
}

.hero-btn:hover {
  transform: translateY(-1px);
}

.hero-btn.primary {
  color: #fff8eb;
  background: #990c18;
  border: 1px solid #990c18;
  box-shadow: 0 5px 15px rgba(142, 13, 24, .18);
}

.hero-btn.secondary {
  color: #990c18;
  background: rgba(255, 249, 237, .35);
  border: 1px solid #b53a35;
}


/* ================= SECTIONS ================= */

.section {
  padding: 72px 0;
}

.pandal-section {
  background: #fffaf1;
}

.section-heading {
  text-align: center;
  margin-bottom: 27px;
}

.eyebrow {
  margin-bottom: 7px;
  color: #a9791b;
  font: 800 .7rem Georgia, serif;
  letter-spacing: .14em;
}

.section-heading h2,
.toilet-card h2 {
  margin: 0;
  color: #8d0d18;
  font: 700 clamp(2rem, 4vw, 2.8rem) Georgia, serif;
}

.section-heading > p:last-child,
.toilet-card > div > p:last-child {
  margin-top: 7px;
  color: #745c52;
  font-size: .92rem;
}


/* ================= SEARCH ================= */

.search-box {
  max-width: 620px;
  margin: 0 auto 30px;
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 0 16px;
  background: #fff;
  border: 1px solid #e1cda7;
  border-radius: 10px;
  box-shadow: 0 5px 16px rgba(95, 35, 25, .06);
}

.search-box span {
  color: #9c111c;
  font-size: 1.4rem;
}

.search-box input {
  width: 100%;
  height: 50px;
  border: 0;
  outline: 0;
  background: transparent;
  color: #40241e;
  font-size: .95rem;
}


/* ================= PANDAL CARDS ================= */

.pandal-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.pandal-card {
  display: flex;
  gap: 15px;
  padding: 15px;
  background: #fff;
  border: 2px solid #eadcc5;
  border-radius: 20px;
  box-shadow: 0 6px 18px rgba(80, 30, 20, .05);
}

.card-number {
  flex: 0 0 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: #980d18;
  color: #f4d47a;
  font: 800 .9rem Georgia, serif;
}

.card-content {
  min-width: 0;
}

.pandal-card h3 {
  margin-bottom: 5px;
  color: #5b251e;
  font: 700 1.05rem Georgia, serif;
}

.pandal-card p {
  color: #745c52;
  font-size: .86rem;
}

.zone {
  display: inline-block;
  margin-top: 7px;
  margin-right: 4px;
  padding: 3px 8px;
  border-radius: 999px;
  background: #f9edcf;
  color: #8b6714;
  font-size: .7rem;
  font-weight: 700;
}

.text-button {
  display: block;
  margin-top: 10px;
  color: #980d18;
  font-weight: 800;
  font-size: .82rem;
  cursor: pointer;
}

.text-button:disabled {
  color: #b08d84;
  cursor: wait;
}

.empty {
  text-align: center;
  color: #805f5f;
}


/* ================= ROUTE PLANNER ================= */

.route-planner-section {
  background: #fff;
  border-top: 1px solid #f1e3c4;
  border-bottom: 1px solid #f1e3c4;
}

/* -- side picker -- */

.route-start-picker {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  max-width: 760px;
  margin: 0 auto 40px;
}

.route-start-option {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 20px;
  background: #fffaf1;
  border: 2px solid #eadcc5;
  border-radius: 16px;
  box-shadow: 0 6px 18px rgba(80, 30, 20, .05);
  text-align: left;
  cursor: pointer;
  transition: border-color .2s ease, transform .2s ease, box-shadow .2s ease, background .2s ease;
}

.route-start-option:hover {
  border-color: #e3b978;
  transform: translateY(-3px);
  box-shadow: 0 12px 26px rgba(80, 30, 20, .1);
}

.route-start-option.active {
  border-color: #980d18;
  background: linear-gradient(135deg, #fdf1e4 0%, #fff 100%);
  box-shadow: 0 14px 30px rgba(152, 13, 24, .18);
}

.route-start-icon {
  flex: 0 0 54px;
  height: 54px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: #f9edcf;
  font-size: 1.6rem;
  transition: background .2s ease, transform .2s ease;
}

.route-start-option.active .route-start-icon {
  background: #980d18;
  transform: scale(1.05);
}

.route-start-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
}

.route-start-text strong {
  color: #5b251e;
  font: 700 1rem Georgia, serif;
}

.route-start-text small {
  color: #8b6a5e;
  font-size: .78rem;
  line-height: 1.35;
}

/* -- sorted route list -- */

.route-pandal-list {
  max-width: 780px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.route-pandal-card {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 18px;
  background: #fff;
  border: 1px solid #eadcc5;
  border-radius: 14px;
  box-shadow: 0 6px 18px rgba(80, 30, 20, .05);
  transition: box-shadow .2s ease, transform .2s ease, border-color .2s ease;
}

.route-pandal-card:hover {
  transform: translateY(-2px);
  border-color: #e3b978;
  box-shadow: 0 12px 26px rgba(80, 30, 20, .1);
}

.route-pandal-rank {
  flex: 0 0 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: linear-gradient(135deg, #c21f39, #980d18);
  color: #f4d47a;
  font: 800 1rem Georgia, serif;
  box-shadow: 0 4px 12px rgba(152, 13, 24, .3);
}

.route-pandal-info {
  min-width: 0;
  flex: 1;
}

.route-pandal-info h3 {
  margin-bottom: 4px;
  color: #5b251e;
  font: 700 1.05rem Georgia, serif;
}

.route-pandal-info p {
  color: #745c52;
  font-size: .86rem;
}

.route-pandal-distance {
  display: inline-block;
  margin-top: 7px;
  margin-left: 4px;
  padding: 3px 9px;
  border-radius: 999px;
  background: #eaf5ec;
  color: #2e7d4f;
  font-size: .7rem;
  font-weight: 700;
}


/* ================= TOILET ================= */

.toilet-section {
  padding-top: 38px;
}
.facility-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}
.toilet-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 25px;
  padding: 28px;
  border: 1px solid #e5d2aa;
  border-radius: 14px;
  background: #fff;
  box-shadow: 0 7px 20px rgba(80,30,20,.05);
}

.toilet-card h2 {
  font-size: 1.9rem;
}


/* ================= FOOTER ================= */

.app-footer {
  background: #43080e;
  color: #f8e9d5;
  border-top: 1px solid #c69c35;
}

.bottom-border {
  height: 12px;
  background: url('/bottom-border.jpg') center / auto 37px repeat-x;
}

.footer-content {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr;
  gap: 50px;
  padding: 42px 0 36px;
}

.footer-about h3 {
  margin-bottom: 10px;
  color: #f4d47a;
  font: 700 1.25rem Georgia, serif;
}

.footer-about p {
  max-width: 360px;
  color: #e8cfc0;
  font: .86rem/1.6 Georgia, serif;
}

.footer-links h4,
.footer-puja h4 {
  margin-bottom: 12px;
  color: #f4d47a;
  font: 700 .95rem Georgia, serif;
}

.footer-links {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.footer-links a {
  color: #f8e9d5;
  font: .85rem Georgia, serif;
  transition: color .18s ease;
}

.footer-links a:hover {
  color: #f4d47a;
}

.footer-puja p {
  margin-top: 6px;
  color: #e8cfc0;
  font: .84rem Georgia, serif;
}

.footer-puja p:first-of-type {
  color: #f4d47a;
  font-weight: 700;
  font-size: .95rem;
}

.footer-bottom {
  border-top: 1px solid rgba(244, 212, 122, .25);
}

.footer-bottom .container {
  min-height: 58px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
  color: #d8bcae;
  font: .75rem Georgia, serif;
}


/* ================= TABLET ================= */

@media (max-width: 850px) {

  .hero {
    grid-template-columns: 1fr;
  }

  .hero-copy {
    min-height: 500px;
    padding: 48px 24px;
  }

  .hero-image-wrap {
    min-height: 390px;
    max-height: 430px;
  }

  .hero-image {
    min-height: 390px;
  }

  .hero-image-wrap::before {
    background:
      linear-gradient(
        180deg,
        #efc889 0%,
        rgba(239,200,137,0) 20%
      );
  }

  nav {
    display: none;
  }

  .menu-button {
    display: block;
  }

  .mobile-menu {
    display: flex;
    flex-direction: column;
    gap: 0;
    padding: 8px 20px 14px;
    border-top: 1px solid #ecd9b7;
  }

  .mobile-menu a {
    padding: 9px 0;
    color: #6a2b24;
    font: 600 .9rem Georgia, serif;
  }

}


/* ================= MOBILE ================= */

@media (max-width: 700px) {

  /* =========================================
     GLOBAL MOBILE
  ========================================= */

  * {
    box-sizing: border-box;
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    overflow-x: hidden;
  }

  .container {
    width: min(100% - 24px, 1120px);
    margin: 0 auto;
  }

  .section {
    padding: 48px 0;
  }

  /* Prevent long text from creating horizontal scroll */
  h1,
  h2,
  h3,
  h4,
  h5,
  p {
    overflow-wrap: break-word;
  }


  /* =========================================
     HEADER / NAVIGATION
  ========================================= */

  .brand {
    font-size: 1.05rem;
    white-space: nowrap;
  }

  header {
    min-height: 58px;
  }

  nav {
    max-width: 100%;
  }

  .desktop-only {
    display: none !important;
  }


  /* =========================================
     HERO SECTION
  ========================================= */

  .hero-copy {
    min-height: 440px;
    padding: 30px 18px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .hero-image-wrap {
    min-height: 300px;
    max-height: 340px;
    overflow: hidden;
  }

  .hero-image {
    min-height: 300px;
    width: 100%;
    object-fit: cover;
  }

  .decorated-title {
    margin-bottom: 16px;
  }

  .decorated-title h1 {
    font-size: 2.55rem;
    line-height: 1.08;
    margin: 0;
  }

  .decorated-title .line {
    width: 24px;
  }

  .hero-description {
    font-size: .86rem;
    line-height: 1.65;
    max-width: 100%;
  }

  .hero-btn {
    min-height: 44px;
    padding: 10px 18px;
    border-radius: 12px;
    font-size: .88rem;
  }


  /* =========================================
     HEADINGS / SECTION TITLES
  ========================================= */

  .section-title {
    margin-bottom: 24px;
  }

  .section-title h2 {
    font-size: 1.75rem;
    line-height: 1.2;
  }

  .section-title p {
    font-size: .85rem;
    line-height: 1.55;
  }


  /* =========================================
     SEARCH / FILTER AREA
  ========================================= */

  input,
  select,
  textarea {
    max-width: 100%;
    font-size: 16px;
  }

  input,
  select {
    min-height: 44px;
    border-radius: 10px;
  }

  textarea {
    border-radius: 12px;
  }


  /* =========================================
     PANDAL GRID
  ========================================= */

  .pandal-grid {
    grid-template-columns: 1fr;
    gap: 14px;
  }

  .pandal-card {
    padding: 16px;
    min-height: auto;
    gap: 12px;
    border-radius: 16px;
  }

  .card-number {
    width: 42px;
    height: 42px;
    min-width: 42px;
    font-size: .85rem;
  }

  .card-content {
    min-width: 0;
  }

  .card-content h3 {
    font-size: 1.05rem;
    line-height: 1.3;
    margin-bottom: 7px;
  }

  .card-content p {
    font-size: .84rem;
    line-height: 1.45;
    margin-bottom: 9px;
  }

  .zone {
    display: inline-block;
    margin: 2px 3px 5px 0;
    font-size: .72rem;
    line-height: 1.3;
  }

  .text-button {
    min-height: 36px;
    padding: 6px 0;
    font-size: .82rem;
  }


  /* =========================================
     SHOW MORE BUTTON
  ========================================= */

  .pandal-grid + div {
    margin-top: 20px !important;
  }

  .pandal-grid + div button {
    min-height: 42px;
    min-width: 140px;
    padding: 9px 20px !important;
    border-radius: 22px !important;
    font-size: .84rem !important;
  }


  /* =========================================
     ROUTE PLANNER
  ========================================= */

  .route-start-picker {
    grid-template-columns: 1fr;
    gap: 12px;
  }

  .route-start-option {
    padding: 15px 16px;
    min-height: 55px;
    border-radius: 14px;
  }

  .route-pandal-card {
    padding: 14px;
    gap: 12px;
    border-radius: 14px;
  }

  .route-pandal-rank {
    flex-basis: 38px;
    width: 38px;
    height: 38px;
    font-size: .9rem;
  }

  .route-pandal-card h3 {
    font-size: .98rem;
    line-height: 1.35;
  }

  .route-pandal-card p {
    font-size: .82rem;
    line-height: 1.45;
  }

  .route-pandal-card .hero-btn {
    width: 100%;
    margin-top: 8px;
  }


  /* =========================================
     LOCATION / ROUTE BUTTONS
  ========================================= */

  button {
    -webkit-tap-highlight-color: transparent;
  }

  button,
  a {
    touch-action: manipulation;
  }

  .hero-btn,
  .text-button {
    cursor: pointer;
  }


  /* =========================================
     TOILET FINDER
  ========================================= */

  .toilet-card {
    flex-direction: column;
    align-items: stretch;
    gap: 14px;
    padding: 16px;
    border-radius: 14px;
  }

  .toilet-card .hero-btn {
    width: 100%;
    min-height: 44px;
  }
  
  .facility-grid {
    grid-template-columns: 1fr;
  }



  /* =========================================
     REVIEW / FORM AREA
  ========================================= */

  form {
    width: 100%;
  }

  form input,
  form select,
  form textarea,
  form button {
    width: 100%;
  }

  form textarea {
    min-height: 120px;
    resize: vertical;
  }


  /* =========================================
     CARDS IN GENERAL
  ========================================= */

  .card,
  .feature-card,
  .review-card {
    border-radius: 16px;
  }


  /* =========================================
     COUNTDOWN
  ========================================= */

  .countdown {
    width: 100%;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
  }

  .countdown > div {
    min-width: 58px;
    padding: 8px 6px;
    border-radius: 12px;
  }


  /*
     IMAGES
 */

  img {
    max-width: 100%;
  }


  /* 
     FOOTER
 */

  .footer-content {
    grid-template-columns: 1fr;
    gap: 26px;
    padding: 35px 0 28px;
  }

  .footer-about p {
    max-width: 100%;
    font-size: .84rem;
    line-height: 1.6;
  }

  .footer-content h3,
  .footer-content h4 {
    margin-bottom: 10px;
  }

  .footer-bottom .container {
    min-height: auto;
    flex-direction: column;
    justify-content: center;
    gap: 6px;
    padding: 15px 12px;
    text-align: center;
  }

  .footer-bottom {
    font-size: .78rem;
  }


  /* 
     SMALL MOBILE - PHONES
   */

  @media (max-width: 420px) {

    .container {
      width: calc(100% - 18px);
    }

    .section {
      padding: 42px 0;
    }

    .hero-copy {
      min-height: 420px;
      padding: 25px 14px;
    }

    .hero-image-wrap {
      min-height: 280px;
      max-height: 310px;
    }

    .hero-image {
      min-height: 280px;
    }

    .decorated-title h1 {
      font-size: 2.25rem;
    }

    .hero-description {
      font-size: .82rem;
    }

    .section-title h2 {
      font-size: 1.55rem;
    }

    .pandal-card {
      padding: 14px;
    }

    .card-number {
      width: 39px;
      height: 39px;
      min-width: 39px;
    }

    .card-content h3 {
      font-size: 1rem;
    }

    .card-content p {
      font-size: .8rem;
    }

    .zone {
      font-size: .68rem;
    }

    .route-pandal-card {
      padding: 12px;
    }

  }

}
</style>