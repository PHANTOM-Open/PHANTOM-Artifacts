# Artifact Appendix: PHANTOM

## Abstract

Artifacts for **"PHANTOM: Undermining Mobile System Availability via Malformed Installation Metadata"**.

Contents:
- Pre-built attack artifacts (APK/IPA)
- Source code for all artifacts
- Crash logs and demonstration videos
- Evaluation spreadsheets (849 tested fields)

## Claims Supported

1. **65 exploitable vectors** (33 Android, 32 iOS) — see `EvaluationResults/`
2. **5 impact levels** (L1-L5) — see artifacts and videos
3. **No code execution required** — examine source code, attack is in metadata only

## Requirements

| Platform | Requirements |
|----------|--------------|
| Android | Android 10+ device, ADB |
| iOS | iOS 15+ device, Xcode, Developer certificate |

## Evaluation Instructions

### Quick Verification (30 min)

**Option 1: Install pre-built APK**
```bash
adb install CrashArtifactAndSourceCode/Android_L2_Partial_Service_Disruption.apk
# Observe effect, then uninstall
```

**Option 2: Build from source**
```bash
unzip CrashArtifactAndSourceCode/Android_L2_Partial_Service_Disruption.zip
# Open in Android Studio and build
```

**Option 3: Review evidence**
- Watch videos in `DemonstrationVideos/`
- Examine logs in `CrashLogs/`

### Full Evaluation

| Claim | Evidence |
|-------|----------|
| 65 vectors | `EvaluationResults/*.xlsx` |
| Impact levels | `CrashArtifactAndSourceCode/` + videos |
| No code execution | Source code - check `AndroidManifest.xml` / `Info.plist` |

## Security Warning

**L3+ attacks cause data loss.** Test only on dedicated devices.
