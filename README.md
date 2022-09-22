# conan-rubberband

My conan recipe for [rubberband](https://breakfastquay.com/rubberband/).

## Manually packaging

```sh
conan source .
conan install .
conan package .
```

Also available on https://osakared.jfrog.io/artifactory/api/conan/osakared as rubberband/56058cc288588bf69048b954aa520e832a071708, try:

```python
self.requires("rubberband/default@rubberband/56058cc288588bf69048b954aa520e832a071708")
```

I hope to clean this up and contribute to conancenter. If I do that, I'll archive this repo.