# PHANTOM: Undermining Mobile System Availability via Malformed Installation Metadata

## Overview

This repository contains artifacts for the paper **"PHANTOM: Undermining Mobile System Availability via Malformed Installation Metadata"**.

PHANTOM is a new class of attacks that exploits malformed package metadata to cause mobile system failures **without executing any code**. We identified **65 exploitable attack vectors** (33 Android, 32 iOS) with impacts ranging from service disruption to persistent boot loops.

## Repository Structure

```
├── CrashArtifactAndSourceCode/    # Pre-built APK/IPA + source code
├── CrashLogs/                     # System crash logs
├── DemonstrationVideos/           # Attack demonstration videos
└── EvaluationResults/             # Evaluation spreadsheets
```

## Impact Levels

| Level | Impact | Recovery |
|-------|--------|----------|
| L1 | Uninstallation Prevention | ADB uninstall |
| L2 | Partial Service Disruption | Reboot |
| L3 | Critical Service Disruption | Factory reset |
| L4 | User Data Loss | Data lost |
| L5 | Complete System Failure | DFU reflash |

## Getting Started

**⚠️ WARNING: L3+ attacks cause data loss. Use test devices only.**

### Quick Test (Android)

```bash
# Install pre-built APK
adb install CrashArtifactAndSourceCode/Android_L2_Partial_Service_Disruption.apk

# Observe SystemUI crash, then clean up
adb uninstall <package_name>
```

### Build from Source

Each artifact has a corresponding `.zip` with source code:

```bash
# Extract and modify as needed
unzip CrashArtifactAndSourceCode/Android_L2_Partial_Service_Disruption.zip

# Build with Android Studio, or use the Python helper script
python Android_L3_Critical_Service_Disruption_build.py
```

### iOS

Install the iOS `.ipa` artifacts by AirDrop (enterprise/developer signing may be required), or install to a connected device using `ios-deploy`:

```bash
ios-deploy -b CrashArtifactAndSourceCode/iOS_L2_Proximal_Attack_By_Airdrop.ipa
```

## Artifacts

| Platform | Files | Source |
|----------|-------|--------|
| Android L1-L5 | `Android_L{1..5}_*.apk` | `Android_L{1..5}_*.zip` |
| iOS L2, L5 | `iOS_L2_Proximal_Attack_By_Airdrop.ipa` | `iOS_Source_Code_and_Builder.zip` |

## Ethical Notice

All vulnerabilities have been responsibly disclosed to Google and Apple. **Do not use maliciously.**

## License

MIT License - see [LICENSE](LICENSE)
